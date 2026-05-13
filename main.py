# from app.audio.analyzer import analyze_song


# result = analyze_song(
#     "data/music/Te louer.mp3"
# )

# print(result)





# from app.library.importer import (
#     import_music_library
# )


# import_music_library(
#     "data/music"
# )





from app.repositories.song_repository import (
    get_all_songs
)

from app.recommendation.recommender import (
    recommend_next_song
)

from app.player.session_manager import (
    start_session
)


library = get_all_songs()

first_song = library[0]

session = start_session(
    first_song
)

recommendation = (
    recommend_next_song(

        current_state={

            "current_bpm":
            session.current_bpm,

            "current_energy":
            session.current_energy,

            "current_key":
            session.current_key,

            "current_mood":
            session.current_mood
        },

        library=library,

        played_songs=
        session.played_songs
    )
)

print("\nNOW PLAYING:")
print(f"{first_song['title']} ({first_song['file_path']})")

print("\nRECOMMENDED:")
print(
    recommendation["song"]["title"]
)

print(
    f"Score:"
    f" {recommendation['score']}"
)

from app.player.audio_player import (
    play_song
)

from app.player.playback_controller import (
    playback_loop
)

# Démarrer la boucle de lecture
playback_loop(
    session,
    library
)





# from app.repositories.song_repository import (
#     get_all_songs
# )

# from app.player.session_manager import (
#     start_session
# )

# from app.player.playback_controller import (
#     playback_loop
# )


# library = get_all_songs()

# first_song = library[4]

# session = start_session(
#     first_song
# )

# playback_loop(
#     session,
#     library
# )