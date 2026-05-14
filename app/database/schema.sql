-- DROP TABLE IF EXISTS table_name;

CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,
    artist TEXT,
    album TEXT,

    duration REAL,

    file_path TEXT NOT NULL UNIQUE,

    genre TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS audio_features (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    song_id INTEGER NOT NULL UNIQUE,

    bpm REAL NOT NULL,

    energy REAL NOT NULL,

    loudness REAL,

    mood TEXT NOT NULL,

    musical_key TEXT NOT NULL,

    camelot_key TEXT NOT NULL,

    analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(song_id)
        REFERENCES songs(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS playlists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    description TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS playlist_songs (
    playlist_id INTEGER NOT NULL,

    song_id INTEGER NOT NULL,

    position INTEGER,

    PRIMARY KEY (playlist_id, song_id),

    FOREIGN KEY(playlist_id)
        REFERENCES playlists(id)
        ON DELETE CASCADE,

    FOREIGN KEY(song_id)
        REFERENCES songs(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    current_song_id INTEGER,

    current_bpm REAL,

    current_energy REAL,

    current_mood TEXT,

    current_key TEXT,

    energy_direction TEXT,

    FOREIGN KEY(current_song_id)
        REFERENCES songs(id)
);

CREATE TABLE IF NOT EXISTS session_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    session_id INTEGER NOT NULL,

    song_id INTEGER NOT NULL,

    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    skipped INTEGER DEFAULT 0,

    FOREIGN KEY(session_id)
        REFERENCES sessions(id)
        ON DELETE CASCADE,

    FOREIGN KEY(song_id)
        REFERENCES songs(id)
        ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_audio_bpm
ON audio_features(bpm);

CREATE INDEX IF NOT EXISTS idx_audio_mood
ON audio_features(mood);

CREATE INDEX IF NOT EXISTS idx_audio_key
ON audio_features(musical_key);

CREATE INDEX IF NOT EXISTS idx_audio_energy
ON audio_features(energy);