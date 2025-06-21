# yt2notes (OpenAI SDK v1.x compatible)

Fully automated tool to extract YouTube transcripts, clean them, and generate topic-organized notes using GPT-4o.

## Features

* Downloads auto-generated subtitles via `yt-dlp`
* Cleans up transcript (removes timestamps, noise)
* Sends transcript to OpenAI API (using latest v1+ SDK)
* Outputs notes to `notes.txt`

## Setup

### 1️⃣ Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/youtube-transcript-notes.git
cd youtube-transcript-notes
```

### 2️⃣ Setup virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate.bat  # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set your OpenAI API Key

* Copy `.env.example` to `.env`
* Fill in your `OPENAI_API_KEY`

## Usage

Run the script with any YouTube URL:

```bash
python main.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Notes will be saved to `notes.txt`.

