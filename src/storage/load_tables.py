from pathlib import Path
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.storage.database import create_connection

PROCESSED_PATH = PROJECT_ROOT / "datasets" / "processed"

connection = create_connection()

users = pd.read_csv(PROCESSED_PATH / "users.csv")
movies = pd.read_csv(PROCESSED_PATH / "movies.csv")
ratings = pd.read_csv(PROCESSED_PATH / "ratings.csv")

users.to_sql("users", connection, if_exists="append", index=False)

movies.to_sql("movies", connection, if_exists="append", index=False)

ratings.to_sql("ratings", connection, if_exists="append", index=False)

connection.commit()

print("Data loaded into SQLite successfully.")

connection.close()