from .base import *

ENV_NAME = 'staging'
# Sync matches rarely on staging since
# both prod and staging are running in the same cluster and compete for resources
SYNC_DELAY_BEFORE_MATCH = 60 * 10
SYNC_DELAY_DURING_MATCH = 5
USE_TZ = False
