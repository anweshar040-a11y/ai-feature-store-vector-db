from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "datasets" / "raw" / "ml-100k"

users = pd.read_csv(
    DATA_PATH / "u.user",
    sep="|",
    names=["user_id", "age", "gender", "occupation", "zip_code"]
)

movies = pd.read_csv(
    DATA_PATH / "u.item",
    sep="|",
    encoding="latin-1",
    header=None
)

ratings = pd.read_csv(
    DATA_PATH / "u.data",
    sep="\t",
    names=["user_id", "movie_id", "rating", "timestamp"]
)

print("\nUsers")
print(users.head())

print("\nMovies")
print(movies.head())

print("\nRatings")
print(ratings.head())

print("\nDataset Shapes")
print("Users:", users.shape)
print("Movies:", movies.shape)
print("Ratings:", ratings.shape)