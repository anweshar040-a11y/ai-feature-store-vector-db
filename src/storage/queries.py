from pathlib import Path
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.storage.database import create_connection

connection = create_connection()

query = """
SELECT
    title,
    rating,
    timestamp
FROM ratings
JOIN movies
ON ratings.movie_id = movies.movie_id
LIMIT 10;
"""

results = pd.read_sql_query(query, connection)

print(results)

connection.close()