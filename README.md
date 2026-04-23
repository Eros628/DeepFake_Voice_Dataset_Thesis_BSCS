# Lightweight Deepfake Voice Detection - Audio Dataset

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