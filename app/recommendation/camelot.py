CAMELOT_MAP = {

    "A Minor": "8A",
    "C Major": "8B",

    "E Minor": "9A",
    "G Major": "9B",

    "B Minor": "10A",
    "D Major": "10B",

    "F# Minor": "11A",
    "A Major": "11B",

    "C# Minor": "12A",
    "E Major": "12B",

    "G# Minor": "1A",
    "B Major": "1B",

    "D# Minor": "2A",
    "F# Major": "2B",

    "A# Minor": "3A",
    "C# Major": "3B",

    "F Minor": "4A",
    "G# Major": "4B",

    "C Minor": "5A",
    "D# Major": "5B",

    "G Minor": "6A",
    "A# Major": "6B",

    "D Minor": "7A",
    "F Major": "7B"
}

def get_camelot_key(
    musical_key
):

    return CAMELOT_MAP.get(
        musical_key
    )