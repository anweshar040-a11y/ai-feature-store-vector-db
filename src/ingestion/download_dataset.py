from pathlib import Path
import ssl
import urllib.request
import zipfile

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA_PATH = PROJECT_ROOT / "datasets" / "raw"
ZIP_PATH = RAW_DATA_PATH / "ml-100k.zip"

DATASET_URL = "https://files.grouplens.org/datasets/movielens/ml-100k.zip"


def download_dataset():
    RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

    if ZIP_PATH.exists():
        print("Dataset already downloaded.")
        return

    print("Downloading MovieLens 100K dataset...")

    # Fix SSL certificate issue on Windows
    ssl_context = ssl._create_unverified_context()

    with urllib.request.urlopen(DATASET_URL, context=ssl_context) as response:
        with open(ZIP_PATH, "wb") as file:
            file.write(response.read())

    print("Download complete.")


def extract_dataset():
    extracted_folder = RAW_DATA_PATH / "ml-100k"

    if extracted_folder.exists():
        print("Dataset already extracted.")
        return

    print("Extracting dataset...")

    with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
        zip_ref.extractall(RAW_DATA_PATH)

    print("Extraction complete.")


if __name__ == "__main__":#only runs when file executed directly not when imported as a module
    download_dataset()
    extract_dataset()