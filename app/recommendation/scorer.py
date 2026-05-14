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

def calculate_harmonic_score(
    current_key,
    candidate_key
):
    """
    Calculate harmonic compatibility using Camelot wheel.
    Camelot keys are in format: "8B", "9A", etc.
    """
    
    if not current_key or not candidate_key:
        return 50
    
    # Same key = perfect match
    if candidate_key == current_key:
        return 100
    
    # Extract number and letter from Camelot key
    try:
        curr_num = int(current_key[:-1])
        curr_letter = current_key[-1]
        cand_num = int(candidate_key[:-1])
        cand_letter = candidate_key[-1]
    except (ValueError, IndexError):
        return 30
    
    # Same number, different letter = very compatible
    if curr_num == cand_num and curr_letter != cand_letter:
        return 80
    
    # Adjacent numbers with different letter = compatible
    if abs(curr_num - cand_num) == 1 and curr_letter != cand_letter:
        return 70
    
    # Handle wheel wrapping (12 to 1)
    if (curr_num == 12 and cand_num == 1) or (curr_num == 1 and cand_num == 12):
        if curr_letter != cand_letter:
            return 70
    
    return 30

def calculate_history_score(
    song_id,
    played_songs
):

    if song_id in played_songs:
        return -100

    return 0

def calculate_beatmatch_score(
    current_bpm,
    candidate_bpm
):

    diff = abs(
        current_bpm -
        candidate_bpm
    )

    if diff <= 3:
        return 100

    if diff <= 6:
        return 80

    if diff <= 10:
        return 60

    return 20

def calculate_final_score(
    tempo_score,
    energy_score,
    mood_score,
    harmonic_score,
    beatmatch_score,
    history_score
):

    return (

        tempo_score * 0.2 +

        energy_score * 0.2 +

        mood_score * 0.15 +

        harmonic_score * 0.2 +

        beatmatch_score * 0.15 +

        history_score * 0.1
    )

