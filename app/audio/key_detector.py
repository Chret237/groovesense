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

    key = KEYS[key_index]

    spectral_centroid = np.mean(
        librosa.feature
        .spectral_centroid(
            y=audio,
            sr=sr
        )
    )

    if spectral_centroid > 2000:
        mode = "Major"

    else:
        mode = "Minor"

    return f"{key} {mode}"