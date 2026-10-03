from pathlib import Path
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.storage.database import create_connection


def get_user_features(user_id):
    connection = create_connection()

    query = """
    SELECT
        user_id,
        movies_watched,
        average_rating,
        rating_std,
        first_rating_date,
        last_rating_date
    FROM user_features
    WHERE user_id = ?
    """

    result = pd.read_sql_query(
        query,
        connection,
        params=(user_id,)
    )

    connection.close()

    return result


def get_movie_features(movie_id):
    connection = create_connection()

    query = """
    SELECT
        movie_id,
        rating_count,
        average_rating,
        rating_std,
        movie_age,
        genre_count
    FROM movie_features
    WHERE movie_id = ?
    """

    result = pd.read_sql_query(
        query,
        connection,
        params=(movie_id,)
    )

    connection.close()

    return result

def validate_user_features(user_id):
    features = get_user_features(user_id)

    if features.empty:
        print(f"No features found for user {user_id}")
        return False

    print(f"Features found for user {user_id}")
    return True

def validate_movie_features(movie_id):
    features = get_movie_features(movie_id)

    if features.empty:
        print(f"No features found for movie {movie_id}")
        return False

    print(f"Features found for movie {movie_id}")
    return True


if __name__ == "__main__":

    print("\nUSER FEATURES")
    user_result = get_user_features(1)
    print(user_result)

    print("\nMOVIE FEATURES")
    movie_result = get_movie_features(1)
    print(movie_result)

    print("\nVALIDATION")
    validate_user_features(1)
    validate_movie_features(1)