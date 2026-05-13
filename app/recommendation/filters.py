def filter_candidates(
    songs,
    current_bpm
):

    candidates = []

    for song in songs:

        bpm_diff = abs(
            song["bpm"] - current_bpm
        )

        if bpm_diff <= 20:
            candidates.append(song)

    return candidates