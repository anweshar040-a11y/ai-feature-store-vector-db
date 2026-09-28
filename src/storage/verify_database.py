from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.storage.database import create_connection

connection = create_connection()
cursor = connection.cursor()

tables = cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
).fetchall()

print("Tables:")
print(tables)

for table in ["users", "movies", "ratings"]:
    rows = cursor.execute(
        f"SELECT COUNT(*) FROM {table};"
    ).fetchone()[0]

    print(f"{table}: {rows}")

connection.close()