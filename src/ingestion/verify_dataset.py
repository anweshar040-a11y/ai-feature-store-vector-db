from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_PATH = PROJECT_ROOT / "datasets" / "processed"

users = pd.read_csv(PROCESSED_PATH / "users.csv")
movies = pd.read_csv(PROCESSED_PATH / "movies.csv")
ratings = pd.read_csv(PROCESSED_PATH / "ratings.csv")

print("USERS")
print(users.info())

print("\nMOVIES")
print(movies.info())

print("\nRATINGS")
print(ratings.info())

print("\nMissing Values")
print(users.isnull().sum())
print(movies.isnull().sum())
print(ratings.isnull().sum())