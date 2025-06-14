import os

GAME_WEEK_ENABLED = os.getenv('FF_GAME_WEEK_ENABLED').lower() == "true" if os.getenv('FF_GAME_WEEK_ENABLED') is not None else False
