# Lightweight Deepfake Voice Detection - Audio Dataset


**About This Dataset:**
This dataset was specifically compiled and utilized for our academic thesis, *LIGHTWEIGHT DEEPFAKE AUDIO DETECTION VIA RESNEXT TO MOBILENETV3 KNOWLEDGE DISTILLATION"* It contains the raw audio files necessary for extracting acoustic features and training our deepfake voice detection models.

Due to GitHub's strict file size limits, the raw audio dataset used for training our models is securely hosted on Kaggle. We have provided an automated script to fetch and extract the heavy audio files directly to your local workspace.

## Prerequisites

1. **Python 3.x** installed.
2. A **Kaggle Account**.

## Setup & Download Instructions

### Step 1: Get Your Kaggle API Token
1. Log in to [Kaggle](https://www.kaggle.com/).
2. Go to your **Settings** (Click your profile picture -> Settings).
3. Scroll down to the **API** section and click **"Create New Token"**.
4. A pop-up window will appear showing your new API Token string (it will start with `KGAT_`). Click the copy icon next to it.

### Step 2: Create a Local `.env` File
In the root directory of this repository, create a new file named exactly `.env` (do not add a .txt extension). 

Open the `.env` file and paste your copied token using this exact format:

```env
KAGGLE_API_TOKEN=KGAT_your_long_token_string_here
```
### Step 3: Run the Script
Open your terminal, navigate to this project folder, and run:

```env
python download_dataset.py
```
The script will automatically read your .env file, authenticate with Kaggle, and extract the dataset into a local ./dataset/ folder for immediate use.

## Troubleshooting & Manual Download
If you encounter any network errors, API authentication issues, or if the script fails to download the heavy audio files, you can easily bypass the script and download the dataset manually:
1. Go directly to our dataset page on Kaggle:
https://www.kaggle.com/datasets/yongski/deepfake-voice-detection-thesis

2. Click the Download button in the top right corner.

3. Once the .zip file is downloaded to your computer, extract its contents.

4. Create a folder named dataset in the root directory of this repository.

5. Move all the extracted audio files into this ./dataset/ folder.

Once the files are in the dataset folder, you can proceed with running the feature extraction and model training scripts as normal!

## Authored By:
EROS PILOTON LUCAGBO
CHERRY LEE HONRADA JIMENEZ
ELLA NORIENNE CADELINÑA DACAPIO 
JOSS EVMAR GALEDO OPEÑA
MARYLENE S. EDER, MIT [Adviser]
