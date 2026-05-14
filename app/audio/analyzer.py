from app.audio.loader import load_audio
from app.audio.bpm import extract_bpm
from app.audio.energy import extract_energy
from app.audio.loudness import extract_loudness
from app.audio.mood_detector import detect_mood
from app.audio.key_detector import detect_key
from app.recommendation.camelot import (
    get_camelot_key
)


def analyze_song(path: str):

    audio, sr = load_audio(path)

    bpm = extract_bpm(audio, sr)

    energy = extract_energy(audio)

    loudness = extract_loudness(audio)

    mood = detect_mood(
        bpm,
        energy
    )

    musical_key = detect_key(
        audio,
        sr
    )

    camelot_key = get_camelot_key(
        musical_key
    )

    return {
        "bpm": bpm,
        "energy": energy,
        "loudness": loudness,
        "mood": mood,
        "key": musical_key,
        "camelot_key": camelot_key
    }