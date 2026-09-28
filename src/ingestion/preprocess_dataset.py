from pathlib import Path
import sys
import pandas as pd

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.ingestion.load_dataset import (
    load_movies,
    load_ratings,
    load_users
)

PROCESSED_PATH = PROJECT_ROOT / "datasets" / "processed"
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

users = load_users()
movies = load_movies()
ratings = load_ratings()

ratings["timestamp"] = pd.to_datetime(
    ratings["timestamp"],
    unit="s"
)

movies["release_date"] = pd.to_datetime(
    movies["release_date"],
    errors="coerce"
)

movies["year"] = movies["release_date"].dt.year

movies["title"] = movies["title"].str.strip()

users.to_csv(PROCESSED_PATH / "users.csv", index=False)
movies.to_csv(PROCESSED_PATH / "movies.csv", index=False)
ratings.to_csv(PROCESSED_PATH / "ratings.csv", index=False)

print("Processed datasets saved successfully.")