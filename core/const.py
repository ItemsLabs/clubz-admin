POSITION_DEFENDER = 'd'
POSITION_MIDFIELDER = 'm'
POSITION_FORWARD = 'f'
POSITION_GOALKEEPER = 'g'
POSITION_SUBSTITUTE = 's'
POSITION_UNKNOWN = 'u'

# Goalkeeper | Wing Back | Defender | Defensive Midfielder | Attacking Midfielder | Midfielder | Striker | Substitute
POSITIONS = (
    (POSITION_DEFENDER, 'Wing Back'),
    (POSITION_DEFENDER, 'Defender'),
    (POSITION_MIDFIELDER, 'Defensive Midfielder'),
    (POSITION_MIDFIELDER, 'Midfielder'),
    (POSITION_MIDFIELDER, 'Attacking Midfielder'),
    (POSITION_FORWARD, 'Striker'),
    (POSITION_GOALKEEPER, 'Goalkeeper'),
    (POSITION_SUBSTITUTE, 'Substitute'),
    (POSITION_UNKNOWN, 'Unknown'),
)

MATCH_STATUS_EMPTY = ''
MATCH_STATUS_UNKNOWN = 'u'
MATCH_STATUS_WAITING = 'w'
MATCH_STATUS_LINEUPS = 'l'
MATCH_STATUS_GAME = 'g'
MATCH_STATUS_ENDED = 'e'
MATCH_STATUS_CANCELLED = 'c'

MATCH_STATUSES = (
    (MATCH_STATUS_EMPTY, 'Empty'),
    (MATCH_STATUS_UNKNOWN, 'Unknown'),
    (MATCH_STATUS_WAITING, 'Waiting'),
    (MATCH_STATUS_LINEUPS, 'Lineups'),
    (MATCH_STATUS_GAME, 'Game'),
    (MATCH_STATUS_ENDED, 'Ended'),
    (MATCH_STATUS_CANCELLED, 'Cancelled'),
)

MATCH_PERIOD_PREGAME = 'p'
MATCH_PERIOD_FIRST_HALF = 'f'
MATCH_PERIOD_HALF_TIME = 'h'
MATCH_PERIOD_SECOND_HALF = 's'
MATCH_PERIOD_BREAK_X1 = 'bx1'
MATCH_PERIOD_FIRST_EXT = 'x1'
MATCH_PERIOD_BREAK_X2 = 'bx2'
MATCH_PERIOD_SECOND_EXT = 'x2'
MATCH_PERIOD_BREAK_P = 'bp'
MATCH_PERIOD_PENALTIES = 'pe'
MATCH_PERIOD_POST_GAME = 'pg'

MATCH_PERIODS = (
    (MATCH_PERIOD_PREGAME, 'Pregame'),
    (MATCH_PERIOD_FIRST_HALF, 'First half'),
    (MATCH_PERIOD_HALF_TIME, 'Half time'),
    (MATCH_PERIOD_SECOND_HALF, 'Second half'),
    (MATCH_PERIOD_BREAK_X1, 'Break x1'),
    (MATCH_PERIOD_FIRST_EXT, 'First ext'),
    (MATCH_PERIOD_BREAK_X2, 'Break x2'),
    (MATCH_PERIOD_SECOND_EXT, 'Second ext'),
    (MATCH_PERIOD_BREAK_P, 'Break penalties'),
    (MATCH_PERIOD_PENALTIES, 'Penalties'),
    (MATCH_PERIOD_POST_GAME, 'Post game'),
)

DEFAULT_MATCH_RULES = {
    'num_of_picks': 4,
    'max_star_player_picks': 2,
}

TIER_NONE = 0
TIER_PREMIUM = 1
TIER_LITE = 2

TIER_CHOICES = (
    (TIER_NONE, 'None'),
    (TIER_PREMIUM, 'Premium'),
    (TIER_LITE, 'Lite'),
)

NFT_CATEGORY_DISTRIBUTION = 'distribution'
NFT_CATEGORY_SHOOTING = 'shooting'
NFT_CATEGORY_PASSING = 'passing'
NFT_CATEGORY_DRIBBLING = 'dribbling'
NFT_CATEGORY_DEFENCE = 'defence'
NFT_CATEGORY_DISCIPLINARY = 'disciplinary'
NFT_CATEGORY_STOPPING = 'stopping'
NFT_CATEGORY_CLAIMING = 'claiming'

NFT_CATEGORIES = (
    (NFT_CATEGORY_DISTRIBUTION, 'distribution'),
    (NFT_CATEGORY_SHOOTING, 'shooting'),
    (NFT_CATEGORY_PASSING, 'passing'),
    (NFT_CATEGORY_DRIBBLING, 'dribbling'),
    (NFT_CATEGORY_DEFENCE, 'defence'),
    (NFT_CATEGORY_DISCIPLINARY, 'disciplinary'),
    (NFT_CATEGORY_STOPPING, 'stopping'),
    (NFT_CATEGORY_CLAIMING, 'claiming'),
)
