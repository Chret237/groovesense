CAMELOT_COMPATIBILITY = {

    "8A": [
        "7A",
        "9A",
        "8B"
    ],

    "9A": [
        "8A",
        "10A",
        "9B"
    ],

    "10A": [
        "9A",
        "11A",
        "10B"
    ]
}

def calculate_harmonic_score(
    current_camelot,
    candidate_camelot
):

    if (
        candidate_camelot
        ==
        current_camelot
    ):
        return 100

    compatible = (
        CAMELOT_COMPATIBILITY.get(
            current_camelot,
            []
        )
    )

    if candidate_camelot in compatible:
        return 85

    return 20