import time

from app.player.audio_player import (
    play_song,
    is_playing
)

from app.recommendation.recommender import (
    recommend_next_song
)

from app.player.session_manager import (
    update_session
)


def playback_loop(
    session,
    library
):

    # Trouver une première chanson valide
    print("[DEBUG] Starting playback loop...")
    while True:
        current_song = session.current_song
        print(f"[DEBUG] Trying to load first song: {current_song.get('title', 'Unknown')} - {current_song.get('file_path', 'Unknown')}")
        song_loaded = play_song(
            current_song["file_path"]
        )
        
        if song_loaded:
            print(
                f"Now Playing: "
                f"{current_song['title']} ({current_song['file_path']})"
            )
            break
        else:
            print(
                f"Skipping corrupted song: "
                f"{current_song['title']} ({current_song['file_path']})"
            )
            print("[DEBUG] Recommending next song...")
            try:
                next_song = (
                    recommend_next_song(
                        current_state={
                            "current_bpm":
                            session.current_bpm,

                            "current_energy":
                            session.current_energy,

                            "current_mood":
                            session.current_mood,

                            "camelot_key":
                            session.current_key
                        },

                        library=library,

                        played_songs=
                        session.played_songs
                    )
                )
                print("\nRECOMMENDED:")
                print(next_song["song"]["title"] + " (" + next_song["song"]["file_path"] + ")")
                print(f"Score: {next_song['score']}")
                update_session(
                    session,
                    next_song["song"]
                )
            except Exception as e:
                print(f"[ERROR] Failed to recommend song: {e}")
                raise

    # Boucle principale de lecture
    print("[DEBUG] Main playback loop started")
    while True:

        while is_playing():
            time.sleep(1)

        print("[DEBUG] Song finished, recommending next song...")
        # Recommander et charger la prochaine chanson
        try:
            next_song = (
                recommend_next_song(
                    current_state={
                        "current_bpm":
                        session.current_bpm,

                        "current_energy":
                        session.current_energy,

                        "current_mood":
                        session.current_mood,

                        "camelot_key":
                        session.current_key
                    },

                    library=library,

                    played_songs=
                    session.played_songs
                )
            )
            print("\nRECOMMENDED:")
            print(next_song["song"]["title"] + " (" + next_song["song"]["file_path"] + ")")
            print(f"Score: {next_song['score']}")
            update_session(
                session,
                next_song["song"]
            )
        except Exception as e:
            print(f"[ERROR] Failed to recommend song: {e}")
            raise

        # Essayer de charger la nouvelle chanson
        # Répéter jusqu'à en trouver une valide
        while True:
            current_song = (
                session.current_song
            )

            print(
                f"Now Playing: "
                f"{current_song['title']} ({current_song['file_path']})"
            )

            song_loaded = play_song(
                current_song["file_path"]
            )

            if song_loaded:
                print("[DEBUG] Song loaded successfully")
                break
            else:
                print(
                    f"Skipping corrupted song: "
                    f"{current_song['title']} ({current_song['file_path']})"
                )
                print("[DEBUG] Recommending replacement song...")
                try:
                    next_song = (
                        recommend_next_song(
                            current_state={
                                "current_bpm":
                                session.current_bpm,

                                "current_energy":
                                session.current_energy,

                                "current_mood":
                                session.current_mood,

                                "camelot_key":
                                session.current_key
                            },

                            library=library,

                            played_songs=
                            session.played_songs
                        )
                    )
                    print("\nRECOMMENDED:")
                    print(next_song["song"]["title"] + " (" + next_song["song"]["file_path"] + ")")
                    print(f"Score: {next_song['score']}")
                    update_session(
                        session,
                        next_song["song"]
                    )
                except Exception as e:
                    print(f"[ERROR] Failed to recommend replacement: {e}")
                    raise