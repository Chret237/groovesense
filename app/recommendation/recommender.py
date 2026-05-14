from app.recommendation.scorer import *
from app.recommendation.ranking import (
    rank_songs
)


def recommend_next_song(
    current_state,
    library,
    played_songs
):

    scored = []

    for song in library:

        # Skip songs that have already been played
        if song["id"] in played_songs:
            continue

        tempo_score = (
            calculate_tempo_score(
                current_state["current_bpm"],
                song["bpm"]
            )
        )

        energy_score = (
            calculate_energy_score(
                current_state["current_energy"],
                song["energy"]
            )
        )

        mood_score = (
            calculate_mood_score(
                current_state["current_mood"],
                song["mood"]
            )
        )

        harmonic_score = (
            calculate_harmonic_score(
                current_state["camelot_key"],
                song["camelot_key"]
            )
        )

        history_score = (
            calculate_history_score(
                song["id"],
                played_songs
            )
        )

        final_score = (
            calculate_final_score(
                tempo_score,
                energy_score,
                mood_score,
                harmonic_score,
                history_score
            )
        )

        scored.append({

            "song": song,
            "score": final_score
        })

    ranked = rank_songs(scored)

    return ranked[0]