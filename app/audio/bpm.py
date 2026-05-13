import librosa


def extract_bpm(audio, sr):

    tempo, _ = librosa.beat.beat_track(
        y=audio,
        sr=sr
    )

    return round(float(tempo), 2)