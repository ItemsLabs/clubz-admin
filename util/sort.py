from core import const


def sort_players(players):
    return sorted(players,
                  key=lambda x: (get_position_sort(x.position), x.jersey_number if x.jersey_number else 999))


def get_position_sort(position):
    if position == const.POSITION_GOALKEEPER:
        return 1
    elif position == const.POSITION_DEFENDER:
        return 2
    elif position == const.POSITION_MIDFIELDER:
        return 3
    elif position == const.POSITION_FORWARD:
        return 4
    else:
        return 5
