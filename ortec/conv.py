from core import const

POSITION_MAP = {
    1: const.POSITION_GOALKEEPER,  # goalkeeper
    2: const.POSITION_DEFENDER,  # sweeper
    3: const.POSITION_DEFENDER,  # left-back
    4: const.POSITION_DEFENDER,  # left-centre-back
    5: const.POSITION_DEFENDER,  # centre-back
    6: const.POSITION_DEFENDER,  # right-centre-back
    7: const.POSITION_DEFENDER,  # right-back
    8: const.POSITION_DEFENDER,  # left-wing-back
    9: const.POSITION_DEFENDER,  # right-wing-back
    10: const.POSITION_MIDFIELDER,  # defensive-midfield-centre-left
    11: const.POSITION_MIDFIELDER,  # defensive-midfield-centre
    12: const.POSITION_MIDFIELDER,  # defensive-midfield-centre-right
    13: const.POSITION_MIDFIELDER,  # left-midfield
    14: const.POSITION_MIDFIELDER,  # left-centre-midfield
    15: const.POSITION_MIDFIELDER,  # centre-midfield
    16: const.POSITION_MIDFIELDER,  # right-centre-midfield
    17: const.POSITION_MIDFIELDER,  # right-midfield
    18: const.POSITION_MIDFIELDER,  # attacking-midfield-left
    19: const.POSITION_MIDFIELDER,  # attacking-midfield-centre-left
    20: const.POSITION_MIDFIELDER,  # attacking-midfield
    21: const.POSITION_MIDFIELDER,  # attacking-midfield-centre-right
    22: const.POSITION_MIDFIELDER,  # attacking-midfield-right
    23: const.POSITION_FORWARD,  # left-winger
    24: const.POSITION_FORWARD,  # second striker
    25: const.POSITION_FORWARD,  # right-winger
    26: const.POSITION_FORWARD,  # centre-forward-left
    27: const.POSITION_FORWARD,  # centre-forward
    28: const.POSITION_FORWARD,  # centre-forward-right
    29: const.POSITION_SUBSTITUTE,  # bench
    30: const.POSITION_UNKNOWN,  # assistent referee
    31: const.POSITION_UNKNOWN,  # fourth official
    32: const.POSITION_UNKNOWN,  # goal line referee
    33: const.POSITION_UNKNOWN,  # referee
}

POSITION_DEFENDER = 'd'
POSITION_MIDFIELDER = 'm'
POSITION_FORWARD = 'f'
POSITION_GOALKEEPER = 'g'
POSITION_SUBSTITUTE = 's'
POSITION_UNKNOWN = 'u'
