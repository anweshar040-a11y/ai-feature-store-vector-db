from pathlib import Path
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.storage.database import create_connection

connection = create_connection()

tables = pd.read_sql_query(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table';
    """,
    connection
)

print("DATABASE TABLES")
print(tables)

print("\nUSER FEATURES")
print(
    pd.read_sql_query(
        "SELECT * FROM user_features LIMIT 5;",
        connection
    )
)

print("\nMOVIE FEATURES")
print(
    pd.read_sql_query(
        "SELECT * FROM movie_features LIMIT 5;",
        connection
    )
)

connection.close()