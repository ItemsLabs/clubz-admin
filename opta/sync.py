import asyncio
import json
import logging
import time
import uuid
import traceback
from contextlib import contextmanager
from datetime import timedelta, datetime

from celery import shared_task
from django.conf import settings
from django.core.cache import cache
from django.db import transaction, IntegrityError
from django.utils import timezone
from django.utils.dateparse import parse_datetime, parse_date
from core import const
from core.models import (
    CompetitionConfig,
    Competition,
    CompetitionEdition,
    CompetitionPhase,
    Team,
    Match,
    Season,
    Player,
    OptaFeedItem,
    OptaFeedItemVersion,
    MatchEvent,
    MatchPlayer,
    SelectionTeamPlayer,
    EventThrottler,
    Sport,
    ChatRoom,
    CustomUser
)
from mobile_api.celery import WSocketEnabled
from rabbit.models import AMQPEvent
from opta.conv import POSITION_MAP
from opta.parser import (
    extract_match_events,
    ActionCancel,
    ActionMatchEnd,
    get_player_by_person_id,
    ActionLineUp,
    ActionPeriodStart,
    ActionPeriodEnd,
    ActionSubstitution,
    ActionGoal, ActionSelfGoal
)
from opta.utils import opta_format_parse_date
from util.events import create_amqp_event_from_match_event

logger = logging.getLogger('opta.sync')

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


def sync_competitions(filterBy=None, sportName=None):
    logger.info(f"[sync_competitions] START {datetime.now()}")

    # TODO: change to be multisport
    if sportName is None:
        sportName = "Soccer"

    sport = Sport.objects.get(name=sportName)

    for competition in settings.OPTA_CLIENT.get_competitions().get('competition'):
        filter = competition.get("competitionCode")
        if filterBy is not None and filterBy != filter:
            continue
        try:
            competition_config_record = CompetitionConfig.objects.get(enabled=True, filter=filter)
        except:
            continue
        if competition_config_record is not None:
            known_name = competition.get("knownName", competition.get("name"))
            name = competition.get("name")
            competition_record = update_or_create(
                Competition,
                import_id=competition.get('id'),
                name=known_name,
                short_name=name,
                updated_at=datetime.now(),
                sport=sport,
                config=competition_config_record
            )
            if competition_config_record.import_id is None:
                competition_config_record.import_id = competition.get('id')
                competition_config_record.name = known_name
                competition_config_record.related_competition = competition_record
                competition_config_record.updated_at = datetime.now()
                competition_config_record.save()
            # for each competition query editions
            for edition in competition.get('tournamentCalendar'):
                start_date = opta_format_parse_date(edition.get("startDate"))
                end_date = opta_format_parse_date(edition.get("endDate"))
                edition_record = update_or_create(
                    CompetitionEdition,
                    import_id=edition.get('id'),
                    name=edition.get("name"),
                    competition=competition_record,
                )
                # for each edition query phases
                season_record = None
                for phase in settings.OPTA_CLIENT.get_competition_phases(edition.get('id')).get('stage', []):
                    update_or_create(
                        CompetitionPhase,
                        import_id=phase.get('id'),
                        name=phase.get("name"),
                        competition_edition=edition_record,
                    )
                    season_record = update_or_create(
                        Season,
                        import_id=phase.get('id'),
                        name=phase.get("name"),
                        start_at=start_date,
                        end_at=end_date,
                    )
                if season_record is None and edition_record is not None:
                    season_record = update_or_create(
                        Season,
                        import_id=edition.get('id'),
                        name=edition.get("name"),
                        start_at=start_date,
                        end_at=end_date,
                    )
                # for each edition query schedule
                for matchDate in settings.OPTA_CLIENT.get_schedule(edition.get('id')).get('matchDate'):
                    for match in matchDate.get('match'):
                        try:
                            # from the match_record, we have homeContestantId (id) homeContestantOfficialName (name), homeContestantCode (abbr)
                            home_team = update_team_record(
                                match.get('homeContestantId'),
                                match.get('homeContestantOfficialName'),
                                match.get('homeContestantCode')
                            )
                            # same with awayContestant
                            away_team = update_team_record(
                                match.get('awayContestantId'),
                                match.get('awayContestantOfficialName'),
                                match.get('awayContestantCode')
                            )
                            d = match.get('date')
                            t = match.get('time')
                            if t is None or t == "":
                                t = "12:00:00Z"
                            dt = parse_datetime(f"{d[:-1] if 'Z' in d else d}T{t + 'Z' if 'Z' not in t else t}")
                            import_id = match.get('id')
                            matchInfo = settings.OPTA_CLIENT.get_match_stats(import_id, "no").get('matchInfo')
                            # -1 can be used to detect those matches that are not regular session (dont have week)
                            week = matchInfo.get('week') or -1
                            match_record = update_or_create(
                                Match,
                                import_id=import_id,
                                competition=competition_record,
                                edition=edition_record,
                                season=season_record,
                                home_team=home_team,
                                away_team=away_team,
                                home_team_selection_id=match.get('homeContestantId'),
                                away_team_selection_id=match.get('awayContestantId'),
                                match_time=dt,
                                match_type=Match.MATCH_TYPE_FREE,  # TODO: remove after beta
                                week=week,
                                sport=sport
                            )
                            update_or_create(ChatRoom,
                                             import_id=import_id,
                                             name=f"{home_team.name} v. {away_team.name} - {dt}",
                                             match=match_record)
                            match_record.sync_match_players()
                        except Exception as e:
                            logger.error("[sync_competitions] {}".format(e))

    logger.info("[sync_competitions] END sync {}".format(datetime.now()))


def update_team_record(id, name, abbr):
    return update_or_create(
        Team,
        import_id=id,
        name=name,
        abbr=abbr
        # opta_selection_id=record.get("Id"),
    )


def sync_all_teams():
    logger.info("[sync_all_teams] start - {}".format(datetime.now()))
    matches = Match.objects.filter(
        home_team_selection_id__isnull=False,
        away_team_selection_id__isnull=False,
        competition_id__isnull=False,
        simulation_from_match_id__isnull=True,
        match_time__gt=timezone.now() - timedelta(hours=10 * 24),
        match_time__lt=timezone.now() + timedelta(hours=30 * 24),
    ).select_related("edition").order_by(
        "-match_time")
    if len(matches) > 0:
        # get a list of a union between away_team_selection_id and home_team_selection_id
        combined_ids_dict = {}
        for match in matches:
            if match.edition.import_id in combined_ids_dict:
                combined_ids_dict[match.edition.import_id].extend(
                    [match.away_team_selection_id, match.home_team_selection_id])
                combined_ids_dict[match.edition.import_id] = list(set(combined_ids_dict[match.edition.import_id]))
            else:
                combined_ids_dict[match.edition.import_id] = [match.away_team_selection_id,
                                                              match.home_team_selection_id]

        for tournamentCalendarUuid in combined_ids_dict:
            for contestantUUID in combined_ids_dict[tournamentCalendarUuid]:
                sync_contestant(tournamentCalendarUuid, contestantUUID)

    logger.info(f"[sync_all_teams] END sync {datetime.now()}")


def sync_contestant(matchImportID, teamSelectionID):
    try:
        team_squad = settings.OPTA_CLIENT.get_selection_persons(matchImportID, teamSelectionID)
    except Exception as e:
        logger.error("[sync_all_teams] - failed to get team squad: {}".format(e))
        return
    for squad in team_squad.get('squad'):
        if squad is not None:
            with transaction.atomic():
                # delete all season team players for team
                SelectionTeamPlayer.objects.filter(selection_id=teamSelectionID).delete()
                for person in squad.get("person", []):
                    if person.get("active") == "no" or person.get("type") != "player":
                        continue
                    first_name = person.get("firstName")
                    last_name = person.get("lastName")
                    nick_name = person.get("matchName")
                    full_name = "{} {}".format(first_name, last_name)

                    player_record = update_or_create(
                        Player,
                        import_id=person.get("id"),
                        first_name=first_name,
                        last_name=last_name,
                        full_name=full_name,
                        nick_name=nick_name,
                        birth_date=parse_date(person.get("dateOfBirth")) if person.get(
                            "dateOfBirth") != None else None,
                        updated_at=datetime.now(),
                    )

                    jersey_number = person.get("shirtNumber")
                    active_selection = person.get("active") == "yes"
                    position = POSITION_MAP.get(person.get("position"))
                    if position is None:
                        logger.warn("[sync_all_teams] person with unknown position: {} - {} ".format(
                            person.get("position"), person.get("id")))
                        position = const.POSITION_UNKNOWN
                    # ignore substitute or unknown positions
                    # if position == const.POSITION_SUBSTITUTE or position == const.POSITION_UNKNOWN:
                    #     continue

                    # try to find season team player, if not exists, create new one
                    try:
                        tp = SelectionTeamPlayer.objects.filter(
                            selection_id=teamSelectionID,
                            player=player_record,
                        ).get()

                        if active_selection:
                            tp.jersey_number = jersey_number
                            tp.position = position
                            tp.updated_at = datetime.now()
                            tp.save()
                        else:
                            tp.delete()

                    except SelectionTeamPlayer.DoesNotExist:
                        if active_selection:
                            # create new season team player, if this doesn't exists
                            SelectionTeamPlayer.objects.create(
                                selection_id=teamSelectionID,
                                player=player_record,
                                jersey_number=jersey_number,
                                position=position,
                            )


@shared_task
def handle_ws_match_event_messages(message):
    match_id = message.get('content').get('liveData').get('matchDetails').get('id')
    try:
        match = Match.objects.get(import_id=match_id)
    except Match.DoesNotExist:
        logger.error("Match with import ID", match_id, "does not exist")
        return
    match_live_data = settings.OPTA_CLIENT.get_match_stats(match_id)
    match_live_data = match_live_data.get('liveData')
    process_event_message(message, match, match_live_data)


def prepare_match_event_items(live_events, match_live_data, match_record):
    items = []
    # print('live_events', live_events)
    # print('match_live_data', match_live_data)
    match_status = match_live_data.get('matchDetails', {}).get('matchStatus', [])
    if len(live_events) > 0:
        period_events = {}
        # store the substitution events in a list
        OPTA_SUBSTITUTION_TYPE_ID = 18  # Player off
        substitution_events = []
        for item in live_events:
            if item.get("typeId") == OPTA_SUBSTITUTION_TYPE_ID:
                substitution_events.append(item)
            # parse events
            match_events = extract_match_events(match_record, item)
            if match_events is None:
                logger.warn("[sync_feed] match_events IS NONE! - item: {}".format(item))
            # modify current period based on ActionPeriodStart event
            for ev in match_events:
                if ev.type == ActionPeriodStart:
                    # get payload and try to understand this period just started
                    if ev.payload:
                        payload = json.loads(ev.payload)
                        if payload and payload.get("period_id"):
                            if period_events.get(payload.get("period_id")) is not None:
                                break
                            period_events[payload.get("period_id")] = ev
                elif ev.type == ActionPeriodEnd:
                    # get payload and try to understand this period just ended
                    if ev.payload:
                        payload = json.loads(ev.payload)
                        if payload and payload.get("period_id"):
                            if period_events.get(payload.get("period_id")) is not None:
                                break
                            period_events[payload.get("period_id")] = ev
                elif ev.type in (ActionGoal, ActionSelfGoal):
                    goal = MatchEvent(item.get('match_events'))

                version_hash = new_version_hash(item)

                unique_id = item.get("id")

                items.append(
                    {
                        "unique_id": unique_id,
                        "event_id": unique_id,
                        "version": version_hash,
                        "match_events": match_events,
                    }
                )

        substitutions = match_live_data.get('substitute')
        # parse sustitutions and make events out of these
        if substitutions is not None:
            for substitution in substitutions:
                player_in = substitution.get("playerOnId")
                player_out = substitution.get("playerOffId")
                team_import_id = substitution.get("contestantId")
                # The players must be stored already, from the lineUps
                player_in_record = get_player_by_person_id(player_in)
                player_out_record = get_player_by_person_id(player_out)
                if player_in_record and player_out_record:
                    # find the substition event where the player in and player out are the same as the substitution event
                    substitution_event = next((x for x in substitution_events if x.get("playerId") == player_out), None)
                    if substitution_event is None:
                        continue
                    # create substitution event
                    mev = MatchEvent()
                    mev.team = Team.objects.get(import_id=team_import_id)
                    mev.type = ActionSubstitution
                    mev.provider_id = str(substitution_event.get("id"))
                    mev.timestamp = substitution.get("timestamp")
                    mev.minute, mev.second = int(substitution.get("timeMinSec").split(":")[0]), int(
                        substitution.get("timeMinSec").split(":")[1])
                    mev.x, mev.y = 0, 0
                    mev.payload = json.dumps(
                        {
                            "player_in_id": str(player_in_record.pk),
                            "player_out_id": str(player_out_record.pk),
                        }
                    )
                    items.append(
                        {
                            "unique_id": mev.provider_id,
                            "event_id": mev.provider_id,
                            "version": "1",
                            "match_events": [mev],
                        }
                    )
                else:
                    logger.warn("[sync_feed] Error: player not found for substitution (in/out): {} {}".format(player_in,
                                                                                                              player_out))
                    logger.warn("[sync_feed] Error: substitution object => {}".format(substitution))

        if len(period_events) > 0:
            if match_status == "Played":
                endEvent = period_events.get(max(period_events.keys()))
                mev = MatchEvent()
                mev.type = ActionMatchEnd
                mev.provider_id = endEvent.provider_id
                mev.timestamp = endEvent.timestamp
                mev.minute, mev.second, mev.x, mev.y = 0, 0, 0, 0
                # insert match ended event
                items.append(
                    {
                        "unique_id": MatchEndEventId,
                        "event_id": MatchEndEventId,
                        "version": "1",
                        "match_events": [mev],
                    }
                )
        return items


def process_event_message(message, match_record, match_live_data):
    live_events = message.get('content').get('liveData').get('matchDetails').get('event', [])
    start_sync = datetime.now()

    items = prepare_match_event_items(live_events, match_live_data, match_record)
    with transaction.atomic():
        # process items inside transaction
        try:
            process_items(match_record, items, delete_not_found_existing=False)
            logger.info("[sync_feed] END  WS sync - import_id: {} - total time: {}".
                        format(match_record.import_id, datetime.now() - start_sync))
        except Exception as e:
            traceback.print_exc()
            logger.error(
                "[sync_feed] - import_id: {} - Error with transaction.atomic: {}".format(match_record.import_id, e))


@shared_task
def start_websocket_listener(import_id):
    cache_id = f"{import_id}-subscribed"

    if cache.get(cache_id):
        print("WebSocket listener is already running.")
        return

    cache.set(cache_id, True, timeout=10800)  # 3hours
    try:
        loop = asyncio.get_event_loop()

        if not loop.is_running():
            print("Starting WebSocket listener.")
            loop.run_until_complete(sync_match_with_ws(import_id))
        else:
            asyncio.run(sync_match_with_ws(import_id))
    finally:
        cache.delete(cache_id)


async def sync_match_with_ws(import_id):
    client = settings.OPTA_WS_CLIENT
    # force_sync_match(Match.objects.get(import_id=import_id))
    await client.connect(import_id, handle_ws_match_event_messages)


def sync_matches(match_time_delta=12, skip_sync_delay=False, competition_code=None, force_SDAPI: bool = False):
    # NOTE: for testing purposes, we can skip sync delay by setting this to True
    # sync feed for all matches within period [now - 12 hours; now + 12 hours]
    dbFilteredMatches = Match.objects.filter(
        match_time__gt=timezone.now() - timedelta(hours=match_time_delta),
        match_time__lt=timezone.now() + timedelta(hours=match_time_delta),
        enabled=True,  # Sync only enabled matches?
    ).order_by("match_time").select_related("competition")
    for match in dbFilteredMatches:
        if not match.competition.enabled:
            # print(f"{match.competition.name} is disabled, skip.")
            continue
        # skip if the competition_code is set and the current match record is NOT from that competition
        if competition_code and match.competition.code != competition_code:
            continue

        if not skip_sync_delay:
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
            sync_match(match, force_SDAPI)
        except Exception as e:
            logger.error(
                "[sync_matches] Error occurred on sync_match {} - {} error: {}".format(match.pk, match.import_id, e))
            import traceback
            traceback.print_exc()

        match.last_synced_at = timezone.now()
        match.save(update_fields=["last_synced_at"])
        # return #to debug step by step just one match


def sync_match(match_record: Match, force_SDAPI: bool = False):
    if match_record.simulation_from_match is not None:
        return

    lock_id = f"{match_record.pk}-lock-{force_SDAPI}"
    print(f"trying to lock {lock_id}, force_SDAPI: {force_SDAPI}")
    with memcache_lock(lock_id, "match-lock") as acquired:
        if acquired:
            print(f"lock {lock_id} acquired")
            # match = load_json_file("opta/api_responses/matchstats_detailed.jsonc")
            match = settings.OPTA_CLIENT.get_match_stats(match_record.import_id)
            sync_feed(match_record, match, force_SDAPI=force_SDAPI)
        else:
            print(f"lock {lock_id} not acquired")


def force_sync_match_with_lock(match_record: Match):
    if match_record.simulation_from_match is not None:
        return

    lock_id = "{0}-lock".format(match_record.pk)
    with memcache_lock(lock_id, "match-lock") as acquired:
        if acquired:
            force_sync_match(match_record)


def force_sync_match(match_record: Match):
    match = settings.OPTA_CLIENT.get_match_stats(match_record.import_id)
    force_sync_feed(match_record, match)


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
        "version": "1",
        "match_events": [mev],
    }


def sync_feed(match_record: Match, matchData: dict, data_feed_sim: bool = False, force_SDAPI: bool = False):
    # THIS IS DIRTY HACK TO AVOID MATCH BEING STUCKED
    if force_SDAPI:
        if match_record.rewarded and match_record.status == const.MATCH_STATUS_GAME:
            logger.error("[sync_feed] MATCH BEING STUCKED, MANUALLY SET ENDED")
            time.sleep(5)
            match_record.refresh_from_db()
            if match_record.rewarded and match_record.status == const.MATCH_STATUS_GAME:
                match_record.status = const.MATCH_STATUS_ENDED
                match_record.save(update_fields=["status"])

    startSync = datetime.now()
    logger.info("[sync_feed] START sync - import_id: {}".format(match_record.import_id))
    matchInfo = matchData.get('matchInfo')
    # print(matchInfo)
    matchLiveData = matchData.get('liveData')
    # print(matchLiveData)
    contestants = matchInfo.get('contestant')
    home_team = None
    away_team = None
    # iterate contestants and figure if there are away and home teams
    for contestant in contestants:
        if contestant.get('position') == "home":
            home_team = contestant
        elif contestant.get('position') == "away":
            away_team = contestant
    # if there is no exactly one home team ans one away team then return with an error message
    if not home_team or not away_team:
        return f"Error: There must be exactly one home team and one away team. match: {match_record.pk} - {match_record.import_id}"
    # if the home team and away team are not the same as the match record then return with an error message
    if home_team.get('id') != match_record.home_team_selection_id or away_team.get(
            'id') != match_record.away_team_selection_id:
        return f"Error: Home team or away team is not the same as the match record. match: {match_record.pk} - {match_record.import_id}"

    # sync home and away team
    if force_SDAPI:
        update_team_record(home_team.get('id'), home_team.get('name'), home_team.get('code'))
        update_team_record(away_team.get('id'), away_team.get('name'), away_team.get('code'))

    matchStatus = matchLiveData.get('matchDetails').get('matchStatus')

    if matchStatus == "Played" or matchStatus == "Playing" or matchStatus == "Fixture":
        items = []
        if force_SDAPI:
            # opta's matchevent object
            home_score = matchLiveData.get('matchDetails').get('scores', {}).get('total', {}).get("home", 0)
            away_score = matchLiveData.get('matchDetails').get('scores', {}).get('total', {}).get("away", 0)
            match_record.home_score = home_score
            match_record.away_score = away_score
            # sync match players, get it from line ups
            home_lineup_players = []
            away_lineup_players = []
            lineups = matchLiveData.get("lineUp", [])
            # save the score right away
            if not data_feed_sim:
                match_record.save(update_fields=['home_score', 'away_score', 'has_lineups'])

            for lineup in lineups:
                selectionEditionId = lineup.get("contestantId")  # team id
                for player in lineup.get("player"):
                    player_record = get_player_by_person_id(player.get("playerId"), player.get("firstName"),
                                                            player.get("lastName"), player.get("matchName"),
                                                            player.get("dateOfBirth"))
                    position = POSITION_MAP.get(player.get("position"))
                    if position is None:
                        position = const.POSITION_UNKNOWN
                    jersey_number = player.get("shirtNumber")

                    if not match_record.is_opta_selection_from_match(selectionEditionId):
                        continue

                    lineup_player = {
                        "id": str(player_record.pk),
                        "jersey_number": jersey_number,
                        "position": position,
                    }
                    if match_record.is_opta_home_selection_from_match(selectionEditionId):
                        home_lineup_players.append(lineup_player)
                    elif match_record.is_opta_away_selection_from_match(selectionEditionId):
                        away_lineup_players.append(lineup_player)

                    # check existence of match player, if it's not exists - create new one
                    try:
                        mp = MatchPlayer.objects.get(player=player_record, match=match_record)
                        if not mp.from_lineups:
                            mp.position = position
                            mp.jersey_number = jersey_number
                            mp.from_lineups = True
                            mp.updated_at = datetime.now()
                            mp.save()

                    except MatchPlayer.DoesNotExist:
                        match_player_team = None
                        if match_record.is_opta_home_selection_from_match(selectionEditionId):
                            match_player_team = match_record.home_team
                        elif match_record.is_opta_away_selection_from_match(selectionEditionId):
                            match_player_team = match_record.away_team

                        if match_player_team:
                            try:
                                MatchPlayer.objects.create(
                                    match=match_record,
                                    player=player_record,
                                    team=match_player_team,
                                    position=position,
                                    jersey_number=jersey_number,
                                    from_lineups=True,
                                )
                            except IntegrityError:
                                pass
                    except MatchPlayer.MultipleObjectsReturned:
                        pass

            # consider each event as item
            if len(home_lineup_players) > 0:
                items.append(
                    make_lineup_item(home_lineup_players, match_record.home_team_id, HomeLineUpEventId)
                )
            if len(away_lineup_players) > 0:
                items.append(
                    make_lineup_item(away_lineup_players, match_record.away_team_id, AwayLineUpEventId)
                )

        if (not force_SDAPI) and WSocketEnabled and matchStatus != "Played" and (
                match_record.simulation_from_match is None):
            match_time = match_record.match_time
            if (match_time - timedelta(minutes=90)) < timezone.now() < (match_time + timedelta(minutes=180)):
                start_websocket_listener.delay(match_record.import_id)
        elif (not WSocketEnabled and matchStatus != "Played") or force_SDAPI:
            live_events = matchLiveData.get("event", None)
            if live_events is None:
                # live_events = load_json_file("opta/api_responses/match_events.jsonc").get('liveData').get('event')
                try:
                    events_from_provider = settings.OPTA_CLIENT.get_match_events(match_record.import_id)
                except:
                    events_from_provider = {}
                live_events = events_from_provider.get('liveData', {}).get('event', [])

            items.extend(prepare_match_event_items(live_events, matchLiveData, match_record))
            with transaction.atomic():
                # process items inside transaction
                try:
                    process_items(match_record, items, data_feed_sim, delete_not_found_existing=not force_SDAPI)
                    logger.info("[sync_feed] END sync - import_id: {} - total time: {}".
                                format(match_record.import_id, datetime.now() - startSync))
                except Exception as e:
                    traceback.print_exc()
                    logger.error(
                        "[sync_feed] - import_id: {} - Error with transaction.atomic: {}".format(match_record.import_id,
                                                                                                 e))
    else:
        print("[sync_feed] match playing nor played. import_id: {} - status {}".format(match_record.import_id,
                                                                                       matchStatus))


def force_sync_feed(match_record: Match, matchData: dict, data_feed_sim: bool = False):
    startSync = datetime.now()
    logger.info("[sync_feed] START FORCE sync - import_id: {}".format(match_record.import_id))
    matchInfo = matchData.get('matchInfo')
    # print(matchInfo)
    matchLiveData = matchData.get('liveData')
    # print(matchLiveData)
    contestants = matchInfo.get('contestant')
    home_team = None
    away_team = None
    # iterate contestants and figure if there are away and home teams
    for contestant in contestants:
        if contestant.get('position') == "home":
            home_team = contestant
        elif contestant.get('position') == "away":
            away_team = contestant
    # if there is no exactly one home team ans one away team then return with an error message
    if not home_team or not away_team:
        return f"Error: There must be exactly one home team and one away team. match: {match_record.pk} - {match_record.import_id}"
    # if the home team and away team are not the same as the match record then return with an error message
    if home_team.get('id') != match_record.home_team_selection_id or away_team.get(
            'id') != match_record.away_team_selection_id:
        return f"Error: Home team or away team is not the same as the match record. match: {match_record.pk} - {match_record.import_id}"

    # sync home and away team
    update_team_record(home_team.get('id'), home_team.get('name'), home_team.get('code'))
    update_team_record(away_team.get('id'), away_team.get('name'), away_team.get('code'))

    matchStatus = matchLiveData.get('matchDetails').get('matchStatus')

    if matchStatus == "Played" or matchStatus == "Playing" or matchStatus == "Fixture":
        # opta's matchevent object
        home_score = matchLiveData.get('matchDetails').get('scores', {}).get('total', {}).get("home", 0)
        away_score = matchLiveData.get('matchDetails').get('scores', {}).get('total', {}).get("away", 0)
        match_record.home_score = home_score
        match_record.away_score = away_score
        # sync match players, get it from line ups
        home_lineup_players = []
        away_lineup_players = []
        lineups = matchLiveData.get("lineUp", [])
        # save the score right away
        if not data_feed_sim:
            match_record.save()
        for lineup in lineups:
            selectionEditionId = lineup.get("contestantId")  # team id
            for player in lineup.get("player"):
                player_record = get_player_by_person_id(player.get("playerId"), player.get("firstName"),
                                                        player.get("lastName"), player.get("matchName"),
                                                        player.get("dateOfBirth"))
                position = POSITION_MAP.get(player.get("position"))
                if position is None:
                    position = const.POSITION_UNKNOWN
                jersey_number = lineup.get("shirtNumber")

                if not match_record.is_opta_selection_from_match(selectionEditionId):
                    continue

                lineup_player = {
                    "id": str(player_record.pk),
                    "jersey_number": jersey_number,
                    "position": position,
                }
                if match_record.is_opta_home_selection_from_match(selectionEditionId):
                    home_lineup_players.append(lineup_player)
                elif match_record.is_opta_away_selection_from_match(selectionEditionId):
                    away_lineup_players.append(lineup_player)

                # check existence of match player, if it's not exists - create new one
                try:
                    mp = MatchPlayer.objects.get(player=player_record, match=match_record)
                    if not mp.from_lineups:
                        mp.position = position
                        mp.jersey_number = jersey_number
                        mp.from_lineups = True
                        mp.updated_at = datetime.now()
                        mp.save()

                except MatchPlayer.DoesNotExist:
                    match_player_team = None
                    if match_record.is_opta_home_selection_from_match(selectionEditionId):
                        match_player_team = match_record.home_team
                    elif match_record.is_opta_away_selection_from_match(selectionEditionId):
                        match_player_team = match_record.away_team

                    if match_player_team:
                        try:
                            MatchPlayer.objects.create(
                                match=match_record,
                                player=player_record,
                                team=match_player_team,
                                position=position,
                                jersey_number=jersey_number,
                                from_lineups=True,
                            )
                        except IntegrityError:
                            pass

        # consider each event as item
        items = []

        if len(home_lineup_players) > 0:
            items.append(
                make_lineup_item(home_lineup_players, match_record.home_team_id, HomeLineUpEventId)
            )
        if len(away_lineup_players) > 0:
            items.append(
                make_lineup_item(away_lineup_players, match_record.away_team_id, AwayLineUpEventId)
            )

        if match_record.simulation_from_match is None:
            live_events = matchLiveData.get("event", None)
            if live_events is None:
                # live_events = load_json_file("opta/api_responses/match_events.jsonc").get('liveData').get('event')
                try:
                    events_from_provider = settings.OPTA_CLIENT.get_match_events(match_record.import_id)
                except:
                    events_from_provider = {}
                live_events = events_from_provider.get('liveData', {}).get('event', [])

            items = prepare_match_event_items(live_events, matchLiveData, match_record)
            with transaction.atomic():
                # process items inside transaction
                try:
                    process_items(match_record, items, data_feed_sim)
                    logger.info("[sync_feed] END sync - import_id: {} - total time: {}".
                                format(match_record.import_id, datetime.now() - startSync))
                except Exception as e:
                    traceback.print_exc()
                    logger.error(
                        "[sync_feed] - import_id: {} - Error with transaction.atomic: {}".format(match_record.import_id,
                                                                                                 e))
    else:
        logger.info("[sync_feed] match playing nor played. import_id: {} - status {}".format(match_record.import_id,
                                                                                             matchStatus))


def process_items(match_record: Match, incoming_events: list, debug: bool = False, delete_not_found_existing=True):
    if incoming_events is None:
        return
    # first of all select all existing items
    existing_items = OptaFeedItem.objects.select_related("current_version").filter(
        match=match_record
    )
    new_added_items = set()

    new_match_events = []
    updated_item_count = 0
    new_item_count = 0

    found_in_incoming = set()

    # handle updated items
    for event in incoming_events:
        existing_item_to_process = None

        # find existing one
        for existing in existing_items:
            if existing.unique_id == str(event.get("unique_id")) and existing.event_id == str(event.get("event_id")):
                # new version for item
                if existing.current_version.version != event.get("version"):
                    existing_item_to_process = existing
                break

        # no changes
        if not existing_item_to_process:
            continue

        # select existing match events for opta_feed_item excluding cancel events
        existing_match_items = MatchEvent.objects.filter(
            opta_feed_item_version=existing_item_to_process.current_version
        )

        to_create, to_delete, non_changed = get_diff_actions(
            existing_match_items, event.get("match_events")
        )

        # calculate status for item
        if len(to_create) == 0 and len(to_delete) == 0:
            new_status = OptaFeedItemVersion.NO_DIFF
        elif len(to_delete) == len(existing_match_items):
            new_status = OptaFeedItemVersion.FULL_CANCEL
        else:
            new_status = OptaFeedItemVersion.PARTIAL_CANCEL

        # update status of item
        existing_item_to_process.current_version.status = new_status
        existing_item_to_process.current_version.save(update_fields=["status"])

        # create new item version
        new_version = OptaFeedItemVersion.objects.create(
            status=OptaFeedItemVersion.ACTIVE,
            version=event.get("version"),
            last_modified_at=timezone.now(),
            item=existing_item_to_process,
        )

        # update reference from item to version
        existing_item_to_process.current_version = new_version
        existing_item_to_process.save(update_fields=["current_version"])

        # generate cancel event actions as part of new version
        for delete_mev in to_delete:
            new_match_events.append(
                generate_cancel_match_event(delete_mev, new_version)
            )

        for mev in to_create:
            mev.opta_feed_item_version = new_version
            new_match_events.append(mev)

        # change link to new version
        for mev in non_changed:
            mev.opta_feed_item_version = new_version
            mev.save(update_fields=["opta_feed_item_version"])

        updated_item_count += 1

    # handle new items
    for event in incoming_events:
        unique_id = event.get("unique_id")
        event_id = event.get("event_id")
        version = event.get("version")

        if unique_id is None:
            logger.info("[process_items] Error: unique_id is None => {}".format(event.get('match_events')[0].type))
            continue

        found = False
        # find existing one
        for existing in existing_items:
            if existing.unique_id == str(unique_id) and existing.event_id == str(event_id):
                found_in_incoming.add(existing.pk)
                found = True
                break

        if found:
            continue

        if event_id in new_added_items:
            continue

        # concurrency issue, continue, will update on next iteration
        if OptaFeedItem.objects.filter(
                unique_id=unique_id,
                event_id=event_id,
                match=match_record,
        ).exists():
            continue

        # insert feed item
        feed_item = OptaFeedItem.objects.create(
            unique_id=unique_id,
            event_id=event_id,
            match=match_record,
        )
        new_added_items.add(event_id)

        # insert version
        feed_item_version = OptaFeedItemVersion.objects.create(
            status=OptaFeedItemVersion.ACTIVE,
            version=version,
            last_modified_at=timezone.now(),
            item=feed_item,
        )

        # update feed link
        feed_item.current_version = feed_item_version
        feed_item.save(update_fields=["current_version"])

        for mev in event.get("match_events"):
            mev.opta_feed_item_version = feed_item_version
            new_match_events.append(mev)

        new_item_count += 1

    # delete items that not found in incoming feed
    deleted_item_count = 0
    deleted_events_count = 0

    if delete_not_found_existing:
        for item in existing_items:
            if item.pk in found_in_incoming:
                continue

            # get all match events for current_version
            active_match_events = (
                MatchEvent.objects.filter(
                    opta_feed_item_version=item.current_version_id,
                    status=MatchEvent.ACTIVE,
                )
                .exclude(type=ActionCancel)
                .all()
            )

            if len(active_match_events) == 0:
                # no match_event to delete, it means this event was already cancelled
                continue

            # update status of item
            if item.current_version is not None:
                item.current_version.status = OptaFeedItemVersion.FULL_CANCEL
                item.current_version.save(update_fields=["status"])

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
            item.save(update_fields=["current_version"])

            for delete_mev in active_match_events:
                new_match_events.append(
                    generate_cancel_match_event(delete_mev, new_version)
                )
                deleted_events_count += 1

            deleted_item_count += 1

    if debug:
        logger.info(f'''[process_items] updated item count: {updated_item_count}
new item count: {new_item_count}
deleted item count: {deleted_item_count}
deleted event count: {deleted_events_count}''')

    # insert match events
    # logger.info("[process_items] new_events len is", len(new_match_events))
    for match_event in new_match_events:
        # empty pk to make sure we're creating new records
        match_event.pk = None
        match_event.match = match_record
        match_event.match_event_id = MatchEvent.objects.filter(match=match_record).count() + 1
        match_event.save()

        # insert amqp event as well
        # TODO: should we disable this? uncommenting the next line will activate:
        create_amqp_event_from_match_event(match_event)


def generate_cancel_match_event(delete_mev, new_version):
    mev = MatchEvent()
    mev.type = ActionCancel
    mev.payload = json.dumps(
        {
            "id": delete_mev.id,
        }
    )
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
    return a.type == b.type and a.points == b.points and a.payload == b.payload


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
                if obj.updated_at is not None:
                    obj.updated_at = datetime.now()
                obj.save()

            return obj

        except cls.DoesNotExist:
            return cls.objects.create(**kwargs)


def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


async def process_match_record(match_record):
    lock_id = "{0}-lock".format(match_record.pk)
    with memcache_lock(lock_id, "match-lock") as acquired:
        if acquired:
            match_stats_api = settings.OPTA_CLIENT.get_match_stats(match_record.import_id)
        week = match_stats_api.get('matchInfo').get('week') or -1
        match_record = update_or_create(
            Match,
            import_id=match_record.import_id,
            week=week,
        )


async def sync_match_no_week():
    import asyncio
    match_records = Match.objects.filter(week=0, simulation_from_match__isnull=True)
    tasks = []
    for match_record in match_records:
        task = asyncio.create_task(process_match_record(match_record))
        tasks.append(task)

    await asyncio.gather(*tasks)


def calculate_unique_id(*args):
    return calculate_hash(*args)[:48]


def calculate_hash(*args):
    # make sure all args are transofrmed to string
    args = [str(arg) for arg in args]
    import hashlib
    concatenated_string = '::'.join(args)
    hash_obj = hashlib.sha512()
    hash_obj.update(concatenated_string.encode('utf-8'))
    return hash_obj.hexdigest()


def process_event_throttling():
    events = EventThrottler.objects.filter(processing=False).order_by('created_at')
    if len(events) > 0:
        sleep_delta = settings.AMQP_THROTTLING_THRESHOLD / len(events)
        EventThrottler.objects.filter(id__in=events).update(processing=True)
        for event in events:
            time.sleep(sleep_delta)
            AMQPEvent.objects.create(
                exchange=event.exchange,
                event_type=event.event_type,
                data=event.data
            )
            event.delete()


def new_version_hash(item):
    lastModified = item.get("lastModified")
    timeStamp = item.get("timeStamp")
    # if the timestamp AND lastModified date string ends with the character "Z", remove it to ensure it's the same as SDDP
    if lastModified and lastModified[-1] == 'Z':
        lastModified = lastModified[:-1]
    if timeStamp and timeStamp[-1] == 'Z':
        timeStamp = timeStamp[:-1]

    parts = [
        item.get("typeId"), item.get("periodId"), item.get("timeMin"), item.get("timeSec"),
        item.get("contestantId"), item.get("playerId"), item.get("outcome"), item.get("assist", "0"),
        timeStamp, lastModified
    ]

    item_qualifiers = item.get("qualifier", [])
    qualifiers = sorted(item_qualifiers, key=lambda x: x.get("qualifierId"))

    paired_qualifiers = [
        f'{q.get("qualifierId", "0")}:{q.get("value", "None")}' for q in qualifiers
    ]

    parts.extend(paired_qualifiers)

    return '#'.join([str(p) for p in parts])
