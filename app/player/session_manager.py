from app.models.session import Session


def start_session(first_song):

    session = Session()

    session.current_song = first_song

    session.current_bpm = first_song["bpm"]

    session.current_energy = (
        first_song["energy"]
    )

    session.current_mood = (
        first_song["mood"]
    )

    session.current_key = (
        first_song["camelot_key"]
    )

    session.played_songs.append(
        first_song["id"]
    )

    return session

def update_session(
    session,
    next_song
):

    session.current_song = next_song

    session.current_bpm = (
        next_song["bpm"]
    )

    session.current_energy = (
        next_song["energy"]
    )

    session.current_mood = (
        next_song["mood"]
    )

    session.current_key = (
        next_song["camelot_key"]
    )

    session.played_songs.append(
        next_song["id"]
    )