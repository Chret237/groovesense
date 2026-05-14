from app.database.connection import (
    get_connection
)

from app.recommendation.camelot import (
    get_camelot_key
)

def insert_audio_features(song_id, features):

    try:
        conn = get_connection()

        cursor = conn.cursor()

        # Convert musical_key to camelot_key
        camelot_key = get_camelot_key(
            features.get("key")
        )

        cursor.execute(
            '''
            INSERT INTO audio_features (
                song_id,
                bpm,
                energy,
                loudness,
                mood,
                musical_key,
                camelot_key
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                song_id,
                features["bpm"],
                features["energy"],
                features["loudness"],
                features["mood"],
                features["key"],
                camelot_key
            )
        )

        conn.commit()

        conn.close()
    except Exception as e:
        print(f"Error inserting audio features: {e}")