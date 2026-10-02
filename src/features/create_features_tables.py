from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.storage.database import create_connection

connection = create_connection()
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_features (
    user_id INTEGER PRIMARY KEY,
    movies_watched INTEGER,
    average_rating REAL,
    rating_std REAL,
    first_rating_date TEXT,
    last_rating_date TEXT,

    FOREIGN KEY(user_id) REFERENCES users(user_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movie_features (
    movie_id INTEGER PRIMARY KEY,
    rating_count INTEGER,
    average_rating REAL,
    rating_std REAL,
    movie_age INTEGER,
    genre_count INTEGER,

    FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
);
""")

connection.commit()

print("Feature tables created successfully.")

connection.close()