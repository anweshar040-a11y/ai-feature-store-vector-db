from pathlib import Path
import sqlite3

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATABASE_PATH = PROJECT_ROOT / "datasets" / "feature_store.db"


def create_connection():
    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute("PRAGMA foreign_keys = ON;")

    return connection


if __name__ == "__main__":
    connection = create_connection()
    print("Connected to SQLite database successfully.")
    connection.close()