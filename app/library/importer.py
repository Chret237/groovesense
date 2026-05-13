from app.library.scanner import (
    scan_music_folder
)

from app.library.metadata import (
    extract_metadata
)

from app.audio.analyzer import (
    analyze_song
)

from app.repositories.song_repository import (
    insert_song
)

from app.repositories.audio_features_repository import (
    insert_audio_features
)


def import_music_library(path):

    songs = scan_music_folder(path)

    for song_path in songs:

        metadata = extract_metadata(
            song_path
        )

        features = analyze_song(
            song_path
        )

        song_data = {
            **metadata,
            "duration": 0,
            "file_path": song_path
        }

        song_id = insert_song(
            song_data
        )

        insert_audio_features(
            song_id,
            features
        )

        print(
            f"Imported: {metadata['title']}"
        )