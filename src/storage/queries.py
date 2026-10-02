from pathlib import Path
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.storage.database import create_connection


connection = create_connection()


# Query 1: Show first 10 ratings with movie titles

query_1 = """
SELECT
    movies.title,
    ratings.rating,
    ratings.timestamp
FROM ratings
JOIN movies
ON ratings.movie_id = movies.movie_id
LIMIT 10;
"""

results_1 = pd.read_sql_query(query_1, connection)

print("\nFIRST 10 RATINGS")
print(results_1)


# Query 2: Find the top-rated movies

query_2 = """
SELECT
    movies.title,
    movie_features.average_rating,
    movie_features.rating_count
FROM movie_features
JOIN movies
ON movie_features.movie_id = movies.movie_id
WHERE movie_features.rating_count >= 20
ORDER BY movie_features.average_rating DESC
LIMIT 10;
"""

results_2 = pd.read_sql_query(query_2, connection)

print("\nTOP-RATED MOVIES")
print(results_2)


# Query 3: Find the most active users

query_3 = """
SELECT
    user_id,
    movies_watched,
    average_rating
FROM user_features
ORDER BY movies_watched DESC
LIMIT 10;
"""

results_3 = pd.read_sql_query(query_3, connection)

print("\nMOST ACTIVE USERS")
print(results_3)


# Query 4: Average rating by occupation

query_4 = """
SELECT
    users.occupation,
    ROUND(AVG(user_features.average_rating), 2) AS average_rating
FROM users
JOIN user_features
ON users.user_id = user_features.user_id
GROUP BY users.occupation
ORDER BY average_rating DESC;
"""

results_4 = pd.read_sql_query(query_4, connection)

print("\nAVERAGE RATING BY OCCUPATION")
print(results_4)


connection.close()