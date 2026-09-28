from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.storage.database import create_connection

connection = create_connection()
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    occupation TEXT,
    zip_code TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    release_date TEXT,
    video_release_date TEXT,
    imdb_url TEXT,

    unknown INTEGER,
    Action INTEGER,
    Adventure INTEGER,
    Animation INTEGER,
    Childrens INTEGER,
    Comedy INTEGER,
    Crime INTEGER,
    Documentary INTEGER,
    Drama INTEGER,
    Fantasy INTEGER,
    FilmNoir INTEGER,
    Horror INTEGER,
    Musical INTEGER,
    Mystery INTEGER,
    Romance INTEGER,
    SciFi INTEGER,
    Thriller INTEGER,
    War INTEGER,
    Western INTEGER,

    year INTEGER
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ratings (
    rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    timestamp TEXT,

    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
);
""")

connection.commit()

print("Database schema created successfully.")

connection.close()