from app.database.connection import (
    get_connection
)

def insert_audio_features(song_id, features):

    try:
        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            '''
            INSERT INTO audio_features (
                song_id,
                bpm,
                energy,
                loudness,
                mood,
                musical_key
            )
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (
                song_id,
                features["bpm"],
                features["energy"],
                features["loudness"],
                features["mood"],
                features["key"]
            )
        )

        conn.commit()

        conn.close()
    except Exception as e:
        print(f"Error inserting audio features: {e}")