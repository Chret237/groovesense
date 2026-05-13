def rank_songs(scored_songs):

    return sorted(
        scored_songs,
        key=lambda x: x["score"],
        reverse=True
    )