from mutagen import File


def extract_metadata(path):

    audio = File(path)

    return {
        "title": str(
            audio.get("TIT2", "Unknown")
        ),

        "artist": str(
            audio.get("TPE1", "Unknown")
        ),

        "album": str(
            audio.get("TALB", "Unknown")
        )
    }