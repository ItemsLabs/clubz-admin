from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

broker_url = 'amqp://{}:{}@{}:{}/{}'.format(
    os.getenv("RMQ_USER"),
    os.getenv("RMQ_PASSWORD"),
    os.getenv("RMQ_HOST"),
    os.getenv("RMQ_PORT"),
    os.getenv("RMQ_VHOST"),
)

WSocketEnabled =  os.getenv('WSOCKET_ENABLED').lower() == "true" if os.getenv('WSOCKET_ENABLED') is not None else False

app = Celery('mobile_api', broker=broker_url)


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sync_competitions': {
        'task': 'core.tasks.task_sync_competitions',
        'schedule': crontab(hour=4, minute=30),  # every day at 04:30
    },
    'task_sync_teams': {
        'task': 'core.tasks.task_sync_teams',
        'schedule': crontab(hour=3, minute=30),  # every day at 03:30
    },
    'task_sync_matches': {
        'task': 'core.tasks.task_sync_matches',
        'schedule': 60 if WSocketEnabled else 5,  # every 5 sec or 60 sec
    },
    'task_sync_match_players': {
        'task': 'core.tasks.task_sync_match_players',
        'schedule': 60 * 60,  # every 1 hour
    },
    'task_process_simulations': {
        'task': 'core.tasks.task_process_simulations',
        'schedule': 30,  # every 30 sec
    },
    'task_sync_soccer_wiki': {
        'task': 'core.tasks.task_sync_soccer_wiki',
        'schedule': 30 * 60,  # every 30 min
    },
    'task_download_soccer_wiki': {
        'task': 'core.tasks.task_download_soccer_wiki',
        'schedule': crontab(hour=4, minute=30),  # every day at 04:30
    },
    'task_update_user_stats': {
        'task': 'core.tasks.task_update_user_stats',
        'schedule': crontab(hour=2, minute=30),  # every day at 02:30
    },
    'task_process_subscription_requests': {
        'task': 'core.tasks.task_process_subscription_requests',
        'schedule': 30,  # every 30 sec
    },
    'task_expire_subscriptions': {
        'task': 'core.tasks.task_expire_subscriptions',
        'schedule': crontab(hour=2, minute=50),  # every day at 02:50
    },
    'task_run_event_throttling': {
        'task': 'core.tasks.task_run_event_throttling',
        'schedule': settings.AMQP_THROTTLING_SCHEDULE_INTERVAL,
    },
    'task_normalize_and_check_all_names': {
        'task': 'core.tasks.task_normalize_and_check_all_names',
        'schedule': crontab(hour=0, minute=0),  # Runs daily at midnight
    },
    'task_conclude_game_week':{
        'task': 'core.tasks.task_conclude_game_week',
        'schedule': 60 * 10,
        # 'schedule': crontab(hour=0, minute=1),  # Runs daily at 00:01
    },
    'task_calculate_promotion_and_relegation':{
        'task': 'core.tasks.task_calculate_promotion_and_relegation',
        # 'schedule': 60 * 6,
        'schedule': 30 * 60,  # every 30 min
    },
    'task_sync_matches_via_sdapi': {
        'task': 'core.tasks.task_sync_matches_via_sdapi',
        'schedule': 60 * 2,  # every 2 minutes (lowest avg SDAPI update)
    },
    # 'task_update_order_statuses': {
    #     'task': 'core.tasks.task_update_order_statuses',
    #     'schedule': 30,  # every 30 sec
    # },
    'task_mint_nfts_for_expired_cardpacks': {
        'task': 'core.tasks.mint_nfts_for_expired_cardpacks',
        'schedule': crontab(minute='*/45'),  # Runs every 45 minutes
    },
    'task_process_pending_crypto_transactions': {
        'task': 'core.tasks.mint_process_pending_crypto_transactions',
        'schedule': crontab(minute='*/15'),  # Runs every 15 minutes
    },
    'task_process_pending_cardpack_transactions': {
        'task': 'core.tasks.mint_process_pending_cardpack_transactions',
        'schedule': crontab(minute='*/15'),  # Runs every 15 minutes
    },
    'assign-default-items-every-10-minutes': {
        'task': 'core.tasks.assign_default_items_to_users_task',
        'schedule': crontab(minute='*/10'),  # Runs every 10 minutes
    }
}
