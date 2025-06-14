from django.conf import settings

from util import events


def update_played_time(match_id):
    events.create_amqp_event(
        settings.AMQP_SYSTEM_EXCHANGE,
        "update_played_time",
        {
            "match_id": match_id,
        }
    )


def validate_positions(positions):
    positions = sorted(positions, key=lambda x: x[0])
    last_max = None

    for i, (min_val, max_val) in enumerate(positions):
        if last_max is not None:
            if min_val > last_max + 1:
                return False
            if last_max is not None and min_val <= last_max:
                return False
        if max_val is None:
            # it should be last range
            if i != len(positions) - 1:
                return False
        last_max = max_val
    return True
