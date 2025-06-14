import json
import logging
import hashlib
import time
import traceback
import uuid
from contextlib import contextmanager
from datetime import timedelta
from django.conf import settings
from django.core.cache import cache
from django.db import transaction, IntegrityError
from django.utils import timezone
from django.utils.dateparse import parse_datetime, parse_date
from core import const
from core.models import Competition, CompetitionEdition, CompetitionPhase, Team, Match, Season, Player, \
    OptaFeedItem, OptaFeedItemVersion, MatchEvent, MatchPlayer, SelectionTeamPlayer
from ortec.conv import POSITION_MAP
from ortec.parser import extract_match_events, ActionCancel, ActionMatchEnd, get_player_by_person_id, \
    ActionLineUp, ActionPeriodStart
from util.events import create_amqp_event_from_match_event

logger = logging.getLogger()

MatchEndEventId = -1
HomeLineUpEventId = -200
AwayLineUpEventId = -201

LOCK_EXPIRE = 60 * 1  # Lock expires in 1 minutes


@contextmanager
def memcache_lock(lock_id, oid):
    timeout_at = time.monotonic() + LOCK_EXPIRE - 3
    # cache.add fails if the key already exists
    status = cache.add(lock_id, oid, LOCK_EXPIRE)
    try:
        yield status
    finally:
        # memcache delete is very slow, but we have to use it to take
        # advantage of using add() for atomic locking
        if time.monotonic() < timeout_at and status:
            # don't release the lock if we exceeded the timeout
            # to lessen the chance of releasing an expired lock
            # owned by someone else
            # also don't release the lock if we didn't acquire it
            cache.delete(lock_id)


def sync_competitions():
    for competition in settings.ORTEC_CLIENT.get_competitions():
        competition_record = update_or_create(
            Competition,
            import_id=competition.get("Id"),
            name=competition.get("Name"),
        )

        # for each competition query editions
        for edition in settings.ORTEC_CLIENT.get_competition_editions(competition.get("Id")):
            edition_record = update_or_create(
                CompetitionEdition,
                import_id=edition.get("Id"),
                name=edition.get("Name"),
                competition=competition_record,
            )

            # for each edition query phases
            for phase in settings.ORTEC_CLIENT.get_competition_phases(edition.get("Id")):
                update_or_create(
                    CompetitionPhase,
                    import_id=phase.get("Id"),
                    name=phase.get("Name"),
                    competition_edition=edition_record,
                )


def sync_registrations():
    phases = CompetitionPhase.objects.filter(
        enabled=True,
        competition_edition__enabled=True,
        competition_edition__competition__enabled=True,
    ).order_by("-created_at", "-import_id").all()

    for phase in phases:
        try:
            sync_phase(phase)
        except Exception:
            print("Cannot sync phase {}".format(phase.pk))
            print(traceback.format_exc())


def sync_phase(phase):
    # query registrations
    for reg in settings.ORTEC_CLIENT.get_registrations(phase.import_id):
        try:
            home_team_record = reg.get("HomeTeam")
            away_team_record = reg.get("AwayTeam")

            home_team = update_team_record(home_team_record)
            away_team = update_team_record(away_team_record)

            # parse date time
            t = parse_datetime(reg.get("DateTime"))

            match = update_or_create(
                Match,
                import_id=reg.get("Id"),
                competition=phase.competition_edition.competition,
                season=Season.current_season(),
                home_team=home_team,
                away_team=away_team,
                home_team_selection_id=home_team_record.get("Id"),
                away_team_selection_id=away_team_record.get("Id"),
                match_time=t,
            )
            match.sync_match_players()
            print("Match {} successfully synced".format(reg.get("Id")))
        except Exception:
            print("Cannot sync match {}".format(reg.get("Id")))
            print(traceback.format_exc())


def update_team_record(record):
    return update_or_create(
        Team,
        import_id=record.get("UId"),
        name=record.get("DisplayName"),
        abbr=record.get("Abbreviation"),
        # ortec_selection_id=record.get("Id"),
    )


def sync_all_teams():
    # delete all season team players before syncing
    SelectionTeamPlayer.objects.all().delete()

    home_selections = list(
        Match.objects.filter(home_team_selection_id__isnull=False).values_list("home_team_selection_id",
                                                                               flat=True).distinct())
    away_selections = list(
        Match.objects.filter(home_team_selection_id__isnull=False).values_list("away_team_selection_id",
                                                                               flat=True).distinct())
    unique_selections = home_selections + list(set(away_selections) - set(home_selections))

    for selection_id in unique_selections:
        try:
            sync_players(selection_id)
        except Exception as e:
            print('Error occurred on sync players for selection {}'.format(selection_id), e)


def sync_players(ortec_selection_id):
    if not ortec_selection_id:
        return

    for person in settings.ORTEC_CLIENT.get_selection_persons(ortec_selection_id):
        first_name = person.get("FirstName")
        last_name = person.get("SurName")
        nick_name = person.get("NickName")

        if nick_name:
            full_name = nick_name
        else:
            full_name = "{} {}".format(first_name, last_name)

        player = update_or_create(
            Player,
            import_id=person.get("Id"),
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            nick_name=nick_name,
            birth_date=parse_date(person.get("DateOfBirth")),
        )

        jersey_number = person.get("DefaultShirtNumber")
        active_selection = person.get("ActiveSelection")
        position = POSITION_MAP.get(int(person.get("DefaultPosition", 0)))

        # ignore substitute or unknown positions
        if position == const.POSITION_SUBSTITUTE or position == const.POSITION_UNKNOWN:
            continue

        # try to find season team player, if not exists, create new one
        try:
            tp = SelectionTeamPlayer.objects.filter(
                selection_id=ortec_selection_id,
                player=player,
            ).get()

            if active_selection:
                tp.jersey_number = jersey_number
                tp.position = position
                tp.save()
            else:
                tp.delete()

        except SelectionTeamPlayer.DoesNotExist:
            if active_selection:
                # create new season team player, if this doesn't exists
                SelectionTeamPlayer.objects.create(
                    selection_id=ortec_selection_id,
                    player=player,
                    jersey_number=jersey_number,
                    position=position,
                )


def sync_matches():
    # sync feed for all matches within period [now - 12 hours; now + 12 hours]
    for match in Match.objects.filter(
            match_time__gt=timezone.now() - timedelta(hours=12),
            match_time__lt=timezone.now() + timedelta(hours=12)).order_by("match_time"):

        now = timezone.now()

        # calculate sync_delay
        if (match.match_time - now) > timedelta(minutes=30):
            # 30 min before match
            sync_delay = timedelta(seconds=settings.SYNC_DELAY_BEFORE_MATCH)
        else:
            sync_delay = timedelta(seconds=settings.SYNC_DELAY_DURING_MATCH)

        if match.last_synced_at and match.last_synced_at > (now - sync_delay):
            continue

        # ignore ended matches
        if match.status == const.MATCH_STATUS_ENDED:
            continue

        # sync match feed
        try:
            sync_match(match)
        except Exception as e:
            print('Error occurred on sync match {}'.format(match.pk), e)

        match.last_synced_at = now
        match.save(update_fields=['last_synced_at'])


def sync_match(match):
    lock_id = '{0}-lock'.format(match.pk)
    with memcache_lock(lock_id, 'match-lock') as acquired:
        if acquired:
            registration_data = settings.ORTEC_CLIENT.get_registration(match.import_id)
            sync_feed(match, registration_data)


def make_lineup_item(players, team_id, event_id):
    mev = MatchEvent()
    mev.type = ActionLineUp
    mev.provider_id = str(event_id)
    mev.timestamp = timezone.now()
    mev.minute, mev.second, mev.x, mev.y = 0, 0, 0, 0
    mev.payload = json.dumps({"players": players})
    mev.team_id = team_id

    return {
        "unique_id": event_id,
        "event_id": event_id,
        "version": '1',
        "match_events": [mev],
    }


def sync_feed(match, body):
    if not body.get("HomeTeam"):
        logger.error("feed do not have HomeTeam field, match {}".format(match.pk))
        return
    elif not body.get("AwayTeam"):
        logger.error("feed do not have AwayTeam field, match {}".format(match.pk))
        return

    # sync home and away team
    update_team_record(body.get("HomeTeam"))
    update_team_record(body.get("AwayTeam"))

    # sync match players, get it from line ups
    home_lineup_players = []
    away_lineup_players = []
    for lineup in body.get("LineUp"):
        player = get_player_by_person_id(lineup.get("Person"))
        selectionEditionId = lineup.get("SelectionEdition")
        position = POSITION_MAP.get(lineup.get("Position"))
        jersey_number = lineup.get("ShirtNumber")

        if not match.is_ortec_selection_from_match(selectionEditionId):
            continue

        lineup_player = {
            "id": str(player.pk),
            "jersey_number": jersey_number,
            "position": position,
        }
        if match.is_ortec_home_selection_from_match(selectionEditionId):
            home_lineup_players.append(lineup_player)
        elif match.is_ortec_away_selection_from_match(selectionEditionId):
            away_lineup_players.append(lineup_player)

        # check existence of match player, if it's not exists - create new one
        try:
            mp = MatchPlayer.objects.get(player=player, match=match)
            if not mp.from_lineups:
                mp.from_lineups = True
                mp.save()

        except MatchPlayer.DoesNotExist:
            match_player_team = None
            if match.is_ortec_home_selection_from_match(selectionEditionId):
                match_player_team = match.home_team
            elif match.is_ortec_away_selection_from_match(selectionEditionId):
                match_player_team = match.away_team

            if match_player_team:
                try:
                    MatchPlayer.objects.create(
                        match=match,
                        player=player,
                        team=match_player_team,
                        position=position,
                        jersey_number=jersey_number,
                        from_lineups=True
                    )
                except IntegrityError:
                    pass

    # consider each event as item
    items = []

    if len(home_lineup_players) > 0:
        items.append(make_lineup_item(home_lineup_players, match.home_team_id, HomeLineUpEventId))
    if len(away_lineup_players) > 0:
        items.append(make_lineup_item(away_lineup_players, match.away_team_id, AwayLineUpEventId))

    current_period = 1
    for item in body.get("Events"):
        # parse events
        match_events = extract_match_events(match, current_period, item)

        # modify current period based on ActionPeriodStart event
        for ev in match_events:
            if ev.type == ActionPeriodStart:
                # get payload and try to understand this period just started
                if ev.payload:
                    payload = json.loads(ev.payload)
                    if payload and payload.get("periodId"):
                        current_period = payload.get("periodId")

        # make consistent hash of item
        if match.import_id == '121829':
            version_hash = hashlib.sha1(json.dumps(item, sort_keys=True).encode('utf8')).hexdigest()
        else:
            version_hash = calculate_hash(item)

        items.append({
            "unique_id": item.get("Id"),
            "event_id": item.get("Id"),
            "version": version_hash,
            "match_events": match_events,
        })

    if body.get("AnalysisFinished"):
        mev = MatchEvent()
        mev.type = ActionMatchEnd
        mev.provider_id = str(MatchEndEventId)
        mev.timestamp = timezone.now()
        mev.minute, mev.second, mev.x, mev.y = 0, 0, 0, 0

        # insert match ended event
        items.append({
            "unique_id": MatchEndEventId,
            "event_id": MatchEndEventId,
            "version": '1',
            "match_events": [mev],
        })

    with transaction.atomic():
        # process items inside transaction
        process_items(match, items)


def process_items(match, incoming_events):
    # first of all select all existing items
    existing_items = OptaFeedItem.objects.select_related('current_version').filter(match=match)

    new_match_events = []
    updated_item_count = 0
    new_item_count = 0

    found_in_incoming = set()

    # handle updated items
    for event in incoming_events:
        existing_item_to_process = None

        # find existing one
        for existing in existing_items:
            if existing.unique_id == event.get("unique_id") and existing.event_id == event.get("event_id"):
                # new version for item
                if existing.current_version.version != event.get("version"):
                    existing_item_to_process = existing
                break

        # no changes
        if not existing_item_to_process:
            continue

        # select existing match events for opta_feed_item excluding cancel events
        existing_match_items = MatchEvent.objects.filter(
            opta_feed_item_version=existing_item_to_process.current_version)

        to_create, to_delete, non_changed = get_diff_actions(existing_match_items, event.get("match_events"))

        # calculate status for item
        if len(to_create) == 0 and len(to_delete) == 0:
            new_status = OptaFeedItemVersion.NO_DIFF
        elif len(to_delete) == len(existing_match_items):
            new_status = OptaFeedItemVersion.FULL_CANCEL
        else:
            new_status = OptaFeedItemVersion.PARTIAL_CANCEL

        # update status of item
        existing_item_to_process.current_version.status = new_status
        existing_item_to_process.current_version.save(update_fields=['status'])

        # create new item version
        new_version = OptaFeedItemVersion.objects.create(
            status=OptaFeedItemVersion.ACTIVE,
            version=event.get("version"),
            last_modified_at=timezone.now(),
            item=existing_item_to_process,
        )

        # update reference from item to version
        existing_item_to_process.current_version = new_version
        existing_item_to_process.save(update_fields=['current_version'])

        # generate cancel event actions as part of new version
        for delete_mev in to_delete:
            new_match_events.append(generate_cancel_match_event(delete_mev, new_version))

        for mev in to_create:
            mev.opta_feed_item_version = new_version
            new_match_events.append(mev)

        # change link to new version
        for mev in non_changed:
            mev.opta_feed_item_version = new_version
            mev.save(update_fields=['opta_feed_item_version'])

        updated_item_count += 1

    # handle new items
    for event in incoming_events:
        unique_id = event.get("unique_id")
        event_id = event.get("event_id")
        version = event.get("version")

        found = False
        # find existing one
        for existing in existing_items:
            if existing.unique_id == unique_id and existing.event_id == event_id:
                found_in_incoming.add(existing.pk)
                found = True
                break

        if found:
            continue

        # insert feed item
        feed_item = OptaFeedItem.objects.create(
            unique_id=unique_id,
            event_id=event_id,
            match=match,
        )

        # insert version
        feed_item_version = OptaFeedItemVersion.objects.create(
            status=OptaFeedItemVersion.ACTIVE,
            version=version,
            last_modified_at=timezone.now(),
            item=feed_item,
        )

        # update feed link
        feed_item.current_version = feed_item_version
        feed_item.save(update_fields=['current_version'])

        for mev in event.get("match_events"):
            mev.opta_feed_item_version = feed_item_version
            new_match_events.append(mev)

        new_item_count += 1

    # delete items that not found in incoming feed
    deleted_item_count = 0
    deleted_events_count = 0

    for item in existing_items:
        if item.pk in found_in_incoming:
            continue

        # get all match events for current_version
        active_match_events = MatchEvent.objects.filter(
            opta_feed_item_version=item.current_version_id,
            status=MatchEvent.ACTIVE,
        ).exclude(type=ActionCancel).all()

        if len(active_match_events) == 0:
            # no match_event to delete, it means this event was already cancelled
            continue

        # update status of item
        item.current_version.status = OptaFeedItemVersion.FULL_CANCEL
        item.current_version.save(update_fields=['status'])

        # create new item version
        new_version = OptaFeedItemVersion.objects.create(
            status=OptaFeedItemVersion.ACTIVE,
            # random uuid as new version
            version=uuid.uuid4(),
            last_modified_at=timezone.now(),
            item=item,
        )

        # update reference from item to version
        item.current_version = new_version
        item.save(update_fields=['current_version'])

        for delete_mev in active_match_events:
            new_match_events.append(generate_cancel_match_event(delete_mev, new_version))
            deleted_events_count += 1

        deleted_item_count += 1

    print("updated item count", updated_item_count)
    print("new item count", new_item_count)
    print("deleted item count", deleted_item_count)
    print("deleted event count", deleted_events_count)

    # calc next match event_id
    next_match_event_id = MatchEvent.objects.filter(match=match).count() + 1

    # insert match events
    print("new_events len is", len(new_match_events))
    for match_event in new_match_events:
        # empty pk to make sure we're creating new records
        match_event.pk = None
        match_event.match = match
        match_event.match_event_id = next_match_event_id
        match_event.save()

        next_match_event_id += 1

        # insert amqp event as well
        create_amqp_event_from_match_event(match_event)


def generate_cancel_match_event(delete_mev, new_version):
    mev = MatchEvent()
    mev.type = ActionCancel
    mev.payload = json.dumps({
        "id": delete_mev.id,
    })
    mev.minute = 0
    mev.second = 0
    mev.opta_feed_item_version = new_version
    mev.timestamp = timezone.now()

    return mev


def get_diff_actions(prev, next):
    # make copy of prev, cause it will be modified
    prev = list(prev)

    to_create = []
    non_changed = []

    for next_event in next:
        # find even in prev
        foundIdx = -1

        for idx, prev_event in enumerate(prev):
            # same event found
            if is_equal(prev_event, next_event):
                foundIdx = idx
                break

        if foundIdx != -1:
            non_changed.append(prev[foundIdx])
            del prev[foundIdx]
        else:
            to_create.append(next_event)

    # all events that are left in prev should be deleted
    to_delete = prev

    return to_create, to_delete, non_changed


def is_equal(a, b):
    # return False
    # #a.get("player_id") == b.get("player_id") and \
    #            #a.get("team_id") == b.get("team_id") and \
    return a.type == b.type and \
           a.points == b.points and \
           a.payload == b.payload


def update_or_create(cls, **kwargs):
    # find pk
    import_id = kwargs.get("import_id")
    with transaction.atomic():
        try:
            obj = cls.objects.select_for_update().get(import_id=import_id)

            changed = False
            for k, v in kwargs.items():
                # check for any change
                if getattr(obj, k) != v:
                    setattr(obj, k, v)
                    changed = True

            # call save only if there was any changes
            if changed:
                obj.save()

            return obj

        except cls.DoesNotExist:
            return cls.objects.create(**kwargs)


def calculate_hash(ev):
    annotations = ev.get('Annotations', [])
    parts = [
        ev.get('DateTime', '')
    ]
    for an in annotations:
        parts.append(calculate_hash_for_annotation(an))
    return '#'.join(parts)


def calculate_hash_for_annotation(ev):
    parts = [
        ev.get('Id', ''),
        ev.get('PersonId', ''),
        ev.get('NextPersonId', ''),
        ev.get('SelectionEditionId', ''),
        ev.get('NextSelectionEdition', ''),
        ev.get('Label', ''),
        ','.join([str(el) for el in ev.get('Properties', [])]),
    ]
    return ';'.join([str(p) for p in parts])
