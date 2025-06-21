import os
import re
import subprocess
import argparse
from dotenv import load_dotenv
import openai

# Load API key from .env
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def download_subtitles(video_url):
    print("Downloading subtitles...")
    subprocess.run([
        "yt-dlp",
        "--write-auto-sub",
        "--sub-lang", "en",
        "--skip-download",
        "-o", "video.%(ext)s",
        video_url
    ], check=True)

    files = [f for f in os.listdir('.') if f.endswith(".vtt")]
    if not files:
        raise Exception("No subtitle file found.")
    return files[0]

def clean_vtt(file_path):
    print("Cleaning transcript...")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    data = re.sub(r"\d{2}:\d{2}:\d{2}\.\d{3} --> .*?\n", "", data)
    data = re.sub(r"NOTE.*?\n", "", data)
    data = re.sub(r"WEBVTT.*?\n", "", data)
    data = re.sub(r"\n{2,}", "\n", data)
    return data.strip()

def generate_notes(transcript):
    print("Generating notes with GPT...")
    max_tokens = 12000
    input_text = transcript[:max_tokens * 4]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a note-taker. Generate concise, topic-organized notes from transcripts. Discard filler."},
            {"role": "user", "content": input_text}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description='YouTube Transcript Notes Generator')
    parser.add_argument('url', type=str, help='YouTube video URL')
    args = parser.parse_args()

    vtt_file = download_subtitles(args.url)
    transcript = clean_vtt(vtt_file)
    notes = generate_notes(transcript)

    with open("notes.txt", "w", encoding='utf-8') as f:
        f.write(notes)
    
    print("\nNotes generated and saved to notes.txt")

if __name__ == "__main__":
    main()