from pathlib import Path
import sys
import pandas as pd
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

ratings = pd.read_csv(
    PROJECT_ROOT / "datasets" / "processed" / "ratings.csv"
)

movies = pd.read_csv(
    PROJECT_ROOT / "datasets" / "processed" / "movies.csv"
)

movie_features = (
    ratings.groupby("movie_id")
    .agg(
        rating_count=("rating", "count"),
        average_rating=("rating", "mean"),
        rating_std=("rating", "std")
    )
    .reset_index()
)

movie_features["rating_std"] = movie_features["rating_std"].fillna(0)

movies["release_date"] = pd.to_datetime(
    movies["release_date"],
    errors="coerce"
)

current_year = datetime.now().year

movies["movie_age"] = current_year - movies["release_date"].dt.year

genre_columns = [
    "unknown","Action","Adventure","Animation","Childrens",
    "Comedy","Crime","Documentary","Drama","Fantasy",
    "FilmNoir","Horror","Musical","Mystery","Romance",
    "SciFi","Thriller","War","Western"
]

movies["genre_count"] = movies[genre_columns].sum(axis=1)

movie_features = movie_features.merge(
    movies[["movie_id","movie_age","genre_count"]],
    on="movie_id",
    how="left"
)

output_path = PROJECT_ROOT / "datasets" / "processed" / "movie_features.csv"

movie_features.to_csv(output_path, index=False)

print(movie_features.head())
print("Movie features created.")