from pathlib import Path
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

ratings = pd.read_csv(
    PROJECT_ROOT / "datasets" / "processed" / "ratings.csv"
)

ratings["timestamp"] = pd.to_datetime(ratings["timestamp"])

user_features = (
    ratings.groupby("user_id")
    .agg(
        movies_watched=("movie_id", "count"),
        average_rating=("rating", "mean"),
        rating_std=("rating", "std"),
        first_rating_date=("timestamp", "min"),
        last_rating_date=("timestamp", "max")
    )
    .reset_index()
)

user_features["rating_std"] = user_features["rating_std"].fillna(0)

output_path = PROJECT_ROOT / "datasets" / "processed" / "user_features.csv"
user_features.to_csv(output_path, index=False)

print(user_features.head())
print("User features created.")