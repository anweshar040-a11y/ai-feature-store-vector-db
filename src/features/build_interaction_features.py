from pathlib import Path
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))


ratings = pd.read_csv(
    PROJECT_ROOT / "datasets" / "processed" / "ratings.csv"
)

user_features = pd.read_csv(
    PROJECT_ROOT / "datasets" / "processed" / "user_features.csv"
)

movie_features = pd.read_csv(
    PROJECT_ROOT / "datasets" / "processed" / "movie_features.csv"
)


interaction_features = ratings[
    ["user_id", "movie_id", "rating"]
].copy()


interaction_features = interaction_features.merge(
    user_features[
        ["user_id", "average_rating", "movies_watched"]
    ],
    on="user_id",
    how="left"
)


interaction_features = interaction_features.merge(
    movie_features[
        ["movie_id", "average_rating", "rating_count"]
    ],
    on="movie_id",
    how="left"
)


interaction_features = interaction_features.rename(
    columns={
        "average_rating_x": "user_average_rating",
        "average_rating_y": "movie_average_rating",
        "movies_watched": "user_activity",
        "rating_count": "movie_popularity"
    }
)


interaction_features["rating_difference"] = (
    interaction_features["user_average_rating"]
    - interaction_features["movie_average_rating"]
)


interaction_features = interaction_features[
    [
        "user_id",
        "movie_id",
        "rating",
        "user_average_rating",
        "movie_average_rating",
        "rating_difference",
        "user_activity",
        "movie_popularity"
    ]
]


output_path = (
    PROJECT_ROOT
    / "datasets"
    / "processed"
    / "interaction_features.csv"
)


interaction_features.to_csv(
    output_path,
    index=False
)


print(interaction_features.head())
print()
print("Interaction features created.")
print("Rows:", len(interaction_features))