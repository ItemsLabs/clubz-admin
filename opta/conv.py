from core import const

# Goalkeeper | Wing Back | Defender | Defensive Midfielder | Attacking Midfielder | Midfielder | Striker | Substitute
POSITION_MAP = {
    "Goalkeeper": const.POSITION_GOALKEEPER,
    "Wing Back": const.POSITION_DEFENDER,
    "Defender": const.POSITION_DEFENDER,
    "Defensive Midfielder": const.POSITION_MIDFIELDER,
    "Attacking Midfielder": const.POSITION_MIDFIELDER,
    "Midfielder": const.POSITION_MIDFIELDER,
    "Striker": const.POSITION_FORWARD,
    "Attacker": const.POSITION_FORWARD,
    "Substitute": const.POSITION_SUBSTITUTE,
}