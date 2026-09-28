from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_PATH = PROJECT_ROOT / "datasets" / "raw" / "ml-100k"


def load_users():
    return pd.read_csv(
        RAW_PATH / "u.user",
        sep="|",
        names=[
            "user_id",
            "age",
            "gender",
            "occupation",
            "zip_code"
        ]
    )


def load_movies():
    movie_columns = [
        "movie_id",
        "title",
        "release_date",
        "video_release_date",
        "imdb_url"
    ]

    genre_columns = [
        "unknown", "Action", "Adventure", "Animation",
        "Childrens", "Comedy", "Crime", "Documentary",
        "Drama", "Fantasy", "FilmNoir", "Horror",
        "Musical", "Mystery", "Romance", "SciFi",
        "Thriller", "War", "Western"
    ]

    columns = movie_columns + genre_columns

    return pd.read_csv(
        RAW_PATH / "u.item",
        sep="|",
        encoding="latin-1",
        names=columns
    )


def load_ratings():
    return pd.read_csv(
        RAW_PATH / "u.data",
        sep="\t",
        names=[
            "user_id",
            "movie_id",
            "rating",
            "timestamp"
        ]
    )


if __name__ == "__main__":
    print(load_users().head())
    print(load_movies().head())
    print(load_ratings().head())