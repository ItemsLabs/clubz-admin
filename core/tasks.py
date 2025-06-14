from datetime import timedelta
from celery.task import task
from celery import shared_task
from django.db import connection
from django.utils import timezone
from core.models import Match, CustomUser
from core.views_inner import process_simulations
# from ortec.sync import sync_competitions, sync_registrations, sync_all_teams, sync_matches
from opta.sync import sync_competitions, sync_all_teams, sync_matches, process_event_throttling
from revenue_cat.sync import process_subscription_requests, expire_subscriptions
from soccer_wiki.sync import sync_players, upload_soccer_wiki_photos
from core.sync import normalize_and_check_all_names
from blockchain_web3.sync import update_order_statuses
from blockchain_web3.tasks import process_mint_nfts_for_expired_cardpacks, process_pending_cardpack_transactions, process_pending_crypto_transactions
import time
from util.events import create_amqp_event
from core.models import CustomUser, GameWeek
from divisions.sync import conclude_game_week, calculate_promotion_and_relegation
from core.notifications import assign_default_items_to_users


@task
def task_sync_competitions(competition_code = None):
    sync_competitions(competition_code)


@task
def task_sync_teams():
    sync_all_teams()


@task
def task_sync_matches(match_time_delta=12, skip_sync_delay = False, competition_code = None):
    sync_matches(match_time_delta, skip_sync_delay, competition_code)


@task
def task_sync_match_players():
    # get upcoming matches for next 3-21 days
    start = timezone.now().today()
    end = start + timedelta(days=21)
    qs = Match.objects.filter(match_time__gte=start, match_time__lt=end).select_related('competition')
    for m in qs:
        if m.competition.enabled: # make sure competition s enabled to sync
            m.sync_match_players(True)


@task
def task_process_simulations():
    process_simulations(None)


def sync_extension(name):
    try:
        with connection.cursor() as cursor:
            cursor.execute("create extension " + name)
    except Exception:
        pass


def make_soccer_wiki_matches():
    sync_extension("unaccent")
    sync_extension("pg_trgm")
    sql = """
    DO $$
    DECLARE
      v_player record;
      v_wiki_player record;
      v_found integer := 0;
      v_not_found integer := 0;
    BEGIN
      PERFORM set_limit(0.3);

      FOR v_player IN SELECT * FROM players WHERE soccer_wiki_player_id is null
      LOOP
        BEGIN
          SELECT swp.*
            INTO STRICT v_wiki_player
            FROM soccer_wiki_players swp
           WHERE (swp.first_name||' '||swp.second_name) % (v_player.first_name||' '||v_player.last_name)
           ORDER BY (swp.first_name||' '||swp.second_name) <-> (v_player.first_name||' '||v_player.last_name) ASC,
                    swp.import_id DESC
           LIMIT 1;

          v_found := v_found + 1;

          UPDATE players
             SET soccer_wiki_player_id = v_wiki_player.id
           WHERE id = v_player.id;
        EXCEPTION
          WHEN no_data_found THEN
            -- RAISE EXCEPTION 'Cannot find soccer_wiki players for (%)', v_player.id;
            v_not_found := v_not_found + 1;
        END;
      END LOOP;
      RAISE NOTICE 'FOUND (%) VS NOT FOUND (%)', v_found, v_not_found;
    END$$;
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)


@task
def task_update_user_stats():
    for user in CustomUser.objects.all()[:999999]:
        user.calculate_stats()


def update_image_url_from_soccer_wiki_players():
    sql = """
update players
   set image_url = soccer_wiki_players.internal_image_url
  from soccer_wiki_players
 where players.soccer_wiki_player_id = soccer_wiki_players.id
   and players.image_url is null
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)


def clear_image_url_for_empty_soccer_wiki_players():
    sql = """
update players
   set image_url = null
 where soccer_wiki_player_id is null
"""
    with connection.cursor() as cursor:
        cursor.execute(sql)


@task
def task_sync_soccer_wiki():
    make_soccer_wiki_matches()
    update_image_url_from_soccer_wiki_players()
    clear_image_url_for_empty_soccer_wiki_players()


@task
def task_download_soccer_wiki():
    print("Downloading soccer wiki")
    sync_players()
    upload_soccer_wiki_photos()
    print("Done downloading soccer wiki")


@task
def task_process_subscription_requests():
    process_subscription_requests()


@task
def task_expire_subscriptions():
    expire_subscriptions()


@task
def task_update_order_statuses():
    return
    # update_order_statuses()

@task
def task_run_event_throttling():
    process_event_throttling()

@task
def task_normalize_and_check_all_names():
    normalize_and_check_all_names()

@task
def task_conclude_game_week():
    ended_game_weeks = GameWeek.objects.filter(end_at__lte=timezone.now(), status=GameWeek.LIVE)
    for week in ended_game_weeks:
        conclude_game_week(week)

@task
def task_calculate_promotion_and_relegation():
    live_weeks = GameWeek.objects.filter(status=GameWeek.LIVE)
    for week in live_weeks:
        calculate_promotion_and_relegation(week)

@task
def task_sync_matches_via_sdapi(match_time_delta=12, skip_sync_delay = False, competition_code = None, force_SDAPI: bool = True):
    sync_matches(match_time_delta, skip_sync_delay, competition_code, force_SDAPI)

@task
def mint_nfts_for_expired_cardpacks():
    process_mint_nfts_for_expired_cardpacks()
    
@task
def mint_process_pending_crypto_transactions():
    process_pending_crypto_transactions()
    
@task
def mint_process_pending_cardpack_transactions():
    process_pending_cardpack_transactions()
    
@task
def assign_default_items_to_users_task():
    assign_default_items_to_users()