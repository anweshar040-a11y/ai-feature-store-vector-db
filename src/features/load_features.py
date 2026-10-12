
from pathlib import Path
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.storage.database import create_connection

connection = create_connection()

processed = PROJECT_ROOT / "datasets" / "processed"

user_features = pd.read_csv(processed / "user_features.csv")
movie_features = pd.read_csv(processed / "movie_features.csv")
interaction_features = pd.read_csv(
    processed / "interaction_features.csv"
)

try:
    # Clear feature records before reloading
    connection.execute("DELETE FROM interaction_features")
    connection.execute("DELETE FROM movie_features")
    connection.execute("DELETE FROM user_features")

    connection.commit()

    user_features.to_sql(
        "user_features",
        connection,
        if_exists="append",
        index=False
    )

    movie_features.to_sql(
        "movie_features",
        connection,
        if_exists="append",
        index=False
    )

    interaction_features.to_sql(
        "interaction_features",
        connection,
        if_exists="append",
        index=False
    )

    connection.commit()
    print("Features loaded into SQLite successfully.")

except Exception:
    connection.rollback()
    raise

finally:
    connection.close()
