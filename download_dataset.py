import os
import subprocess
import sys

# TODO: Replace with your actual Kaggle dataset path 
# Example: "johndoe/deepfake-voice-dataset"
KAGGLE_DATASET = "yongski/deepfake-voice-detection-thesis"
DOWNLOAD_DIR = "./dataset"

def install_kaggle():
    """Ensures the Kaggle API library is installed."""
    print("Checking for Kaggle API library...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "kaggle", "--quiet"])

def download_data():
    """Downloads and unzips the dataset using the Kaggle CLI."""
    print(f"Downloading dataset '{KAGGLE_DATASET}' to '{DOWNLOAD_DIR}'...")
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    
    try:
        # Using subprocess to call the CLI gives us a nice progress bar for large GB files
        subprocess.run([
            "kaggle", "datasets", "download", "-d", KAGGLE_DATASET,
            "-p", DOWNLOAD_DIR, "--unzip"
        ], check=True)
        print("\nSuccess! Your audio files are downloaded, unzipped, and ready for feature extraction.")
    except subprocess.CalledProcessError:
        print("\nError: Failed to download dataset.")
        print("Please ensure your kaggle.json token is correctly placed in your user directory.")

if __name__ == "__main__":
    install_kaggle()
    download_data()