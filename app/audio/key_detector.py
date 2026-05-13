import librosa
import numpy as np

KEYS = [
    "C",
    "C#",
    "D",
    "D#",
    "E",
    "F",
    "F#",
    "G",
    "G#",
    "A",
    "A#",
    "B"
]


def detect_key(
    audio,
    sr
):

    chroma = (
        librosa.feature.chroma_stft(
            y=audio,
            sr=sr
        )
    )

    chroma_mean = np.mean(
        chroma,
        axis=1
    )

    key_index = np.argmax(
        chroma_mean
    )

    return KEYS[key_index]