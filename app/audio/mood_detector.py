def detect_mood(
    bpm,
    energy
):

    if bpm < 80 and energy < 0.2:
        return "calm"

    elif bpm < 100 and energy < 0.5:
        return "chill"

    elif bpm < 120 and energy < 0.8:
        return "groovy"

    else:
        return "dance"