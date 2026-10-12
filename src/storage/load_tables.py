
from pathlib import Path
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.storage.database import create_connection

connection = create_connection()
processed = PROJECT_ROOT / "datasets" / "processed"

users = pd.read_csv(processed / "users.csv")
movies = pd.read_csv(processed / "movies.csv")
ratings = pd.read_csv(processed / "ratings.csv")

try:
    # Find which tables already exist in the database.
    existing_tables = {
        row[0]
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        )
    }

    # Delete dependent records before their parent records.
    tables_to_clear = [
        "interaction_features",
        "movie_features",
        "user_features",
        "ratings",
        "movies",
        "users"
    ]

    for table in tables_to_clear:
        if table in existing_tables:
            connection.execute(f"DELETE FROM {table}")

    connection.commit()

    # Load the raw dataset in parent-to-child order.
    users.to_sql("users", connection, if_exists="append", index=False)
    movies.to_sql("movies", connection, if_exists="append", index=False)
    ratings.to_sql("ratings", connection, if_exists="append", index=False)

    connection.commit()
    print("Users, movies, and ratings loaded successfully.")

except Exception:
    connection.rollback()
    raise

finally:
    connection.close()
