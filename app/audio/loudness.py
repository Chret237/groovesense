import numpy as np


def extract_loudness(audio):

    loudness = np.mean(np.abs(audio))

    return round(float(loudness), 4)