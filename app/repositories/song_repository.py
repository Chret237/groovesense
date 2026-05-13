from app.database.connection import (
    get_connection
)


def insert_song(song_data):

    try:
        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("SELECT id FROM songs WHERE file_path = ?", (song_data["file_path"],))

        existing = cursor.fetchone()

        if existing:
            conn.close()
            return existing[0]

        cursor.execute(
            '''
            INSERT INTO songs (
                title,
                artist,
                album,
                duration,
                file_path
            )
            VALUES (?, ?, ?, ?, ?)
            ''',
            (
                song_data["title"],
                song_data["artist"],
                song_data["album"],
                song_data["duration"],
                song_data["file_path"]
            )
        )

        conn.commit()

        song_id = cursor.lastrowid

        conn.close()

        return song_id
    except Exception as e:
        print(f"Error inserting song: {e}")
        return None


def get_all_songs():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT
            songs.id,
            songs.title,
            songs.artist,
            songs.file_path,

            audio_features.bpm,
            audio_features.energy,
            audio_features.loudness,
            audio_features.mood,
            audio_features.musical_key

        FROM songs

        JOIN audio_features

        ON songs.id =
        audio_features.song_id
        '''
    )

    rows = cursor.fetchall()

    conn.close()

    songs = []

    for row in rows:

        songs.append({

            "id": row[0],
            "title": row[1],
            "artist": row[2],
            "file_path": row[3],

            "bpm": row[4],
            "energy": row[5],
            "loudness": row[6],
            "mood": row[7],
            "musical_key": row[8]
        })

    return songs