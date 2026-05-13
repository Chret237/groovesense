import librosa
import numpy as np


def extract_energy(audio):

    rms = librosa.feature.rms(y=audio)

    energy = np.mean(rms)

    return round(float(energy), 4)