import librosa


def load_audio(path: str):

    audio, sr = librosa.load(
        path,
        sr=22050,
        mono=True
    )

    return audio, sr