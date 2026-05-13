def calculate_tempo_score(
    current_bpm,
    candidate_bpm
):

    diff = abs(
        current_bpm - candidate_bpm
    )

    score = max(
        0,
        100 - diff * 5
    )

    return score

def calculate_energy_score(
    current_energy,
    candidate_energy
):

    diff = abs(
        current_energy -
        candidate_energy
    )

    score = max(
        0,
        100 - diff * 100
    )

    return score

MOOD_COMPATIBILITY = {

    ("calm", "calm"): 100,
    ("calm", "chill"): 80,
    ("calm", "dance"): 20,

    ("groovy", "groovy"): 100,
    ("groovy", "dance"): 75,

    ("dance", "dance"): 100,
}

def calculate_mood_score(
    current_mood,
    candidate_mood
):

    return MOOD_COMPATIBILITY.get(
        (
            current_mood,
            candidate_mood
        ),
        50
    )

HARMONIC_COMPATIBILITY = {

    "C": ["G", "F", "Am"],
    "G": ["D", "C", "Em"],
    "D": ["A", "G", "Bm"],
    "A": ["E", "D", "F#m"],
}

def calculate_harmonic_score(
    current_key,
    candidate_key
):

    if candidate_key == current_key:
        return 100

    compatible = (
        HARMONIC_COMPATIBILITY.get(
            current_key,
            []
        )
    )

    if candidate_key in compatible:
        return 80

    return 30

def calculate_history_score(
    song_id,
    played_songs
):

    if song_id in played_songs:
        return -100

    return 0

def calculate_final_score(
    tempo_score,
    energy_score,
    mood_score,
    harmonic_score,
    history_score
):

    return (

        tempo_score * 0.4 +

        energy_score * 0.3 +

        mood_score * 0.2 +

        harmonic_score * 0.2 +

        history_score * 0.1
    )

