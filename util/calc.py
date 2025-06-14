def get_rank_dict(values):
    values = sorted(values, reverse=True)

    val_dict = dict()
    position, real_position = 0, 0
    prev_score = None
    for val in values:
        real_position += 1
        if prev_score != val:
            position = real_position
        prev_score = val

        val_dict[val] = position

    return val_dict
