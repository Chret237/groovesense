def adjust_target_bpm(
    current_bpm,
    direction
):

    if direction == "INCREASING":
        return current_bpm + 5

    elif direction == "DECREASING":
        return current_bpm - 5

    return current_bpm

def update_energy_direction(
    session,
    direction
):

    session.energy_direction = (
        direction
    )