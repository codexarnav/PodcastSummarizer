# Podcast Summarization Tool

## 📌 Overview
This tool allows you to download a podcast from YouTube, transcribe the audio using **AssemblyAI**, and generate a concise summary using **Facebook's BART model**.

## 🚀 Features
- **Download** podcasts from YouTube as MP3
- **Transcribe** the audio using AssemblyAI
- **Summarize** the transcription using BART Transformer
- **Save** the transcript and summary as text files

## 🛠️ Setup & Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/podcast-summarizer.git
cd podcast-summarizer
```

### 2️⃣ Install Dependencies
Make sure you have **Python 3.8+** installed. Then, run:
```bash
pip install -r requirements.txt
```
Install additional libraries manually if needed:
```bash
pip install yt-dlp assemblyai transformers torch
```

### 3️⃣ Set Up AssemblyAI API Key
Replace `Your_api_key` in the script with your actual **AssemblyAI API key**.

## 🎯 Usage
Run the script by executing:
```bash
python podcast_summarizer.py
```

## 📂 Output Files
- `podcast_audio.mp3` → Extracted audio file
- `podcast_transcript.txt` → Full transcribed text
- `summary.txt` → AI-generated summary

## 🔧 Customization
- Change `podcast_url` in the script to a different YouTube URL to summarize a different podcast.
- Adjust `max_length` and `min_length` in `model.generate()` to tweak the summary length.

## 📜 License
This project is open-source under the **MIT License**.

## 🙌 Contributing
Pull requests are welcome! If you have any suggestions, feel free to open an issue.

---

Happy Summarizing! 🎧📜

