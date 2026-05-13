def mark_song_skipped(
    session,
    song_id
):

    session.skipped_songs.append(
        song_id
    )