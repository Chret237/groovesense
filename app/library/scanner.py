import os


SUPPORTED_FORMATS = (
    ".mp3",
    ".wav"
)


def scan_music_folder(path):

    songs = []

    for root, _, files in os.walk(path):

        for file in files:

            if file.lower().endswith(
                SUPPORTED_FORMATS
            ):

                full_path = os.path.join(
                    root,
                    file
                )

                songs.append(full_path)

    return songs