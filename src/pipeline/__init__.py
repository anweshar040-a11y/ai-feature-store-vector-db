from pathlib import Path
import sys
import subprocess


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def run_script(script_path):
    print()
    print("=" * 60)
    print(f"RUNNING: {script_path}")
    print("=" * 60)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT
    )

    if result.returncode != 0:
        print()
        print(f"Pipeline stopped because {script_path} failed.")
        sys.exit(result.returncode)


def main():

    scripts = [
        PROJECT_ROOT / "src" / "ingestion" / "preprocess_dataset.py",

        PROJECT_ROOT / "src" / "storage" / "schema.py",
        PROJECT_ROOT / "src" / "storage" / "load_tables.py",

        PROJECT_ROOT / "src" / "features" / "create_feature_tables.py",

        PROJECT_ROOT / "src" / "features" / "build_user_features.py",
        PROJECT_ROOT / "src" / "features" / "build_movie_features.py",
        PROJECT_ROOT / "src" / "features" / "build_interaction_features.py",

        PROJECT_ROOT / "src" / "features" / "load_features.py",

        PROJECT_ROOT / "src" / "storage" / "verify_database.py",
        PROJECT_ROOT / "src" / "features" / "verify_features.py"
    ]

    print()
    print("STARTING FEATURE STORE PIPELINE")
    print("=" * 60)

    for script in scripts:
        run_script(script)

    print()
    print("=" * 60)
    print("FEATURE STORE PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()