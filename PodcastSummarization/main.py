import yt_dlp
import assemblyai as aai
import transformers
from transformers import BartTokenizer, BartForConditionalGeneration


model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

def download_podcast(url, output_path="podcast_audio.mp3"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
        'outtmpl': output_path
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_path  

def transcribe(audio_file):
    aai.settings.api_key = 'Your_api_key'
    transcriber = aai.Transcriber()
    
    
    transcript = transcriber.transcribe(audio_file)  
    
    with open('podcast_transcript.txt', 'w', encoding='utf-8') as f:
        f.write(transcript.text)
    
    return transcript.text 

def summarize(text):
    input_ids = tokenizer.encode(text, return_tensors='pt', max_length=1024, truncation=True)
    summary_ids = model.generate(input_ids, max_length=150, min_length=30, length_penalty=2.0, num_beams=4)
    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return output


podcast_url = "https://www.youtube.com/watch?v=6grun0mNktA"
audio_file = download_podcast(podcast_url)


transcribed_text = transcribe(audio_file)


summary = summarize(transcribed_text)


with open('summary.txt', 'w', encoding='utf-8') as f:
    f.write(summary)

print("Summary Generated Successfully! 🚀")

    
  
  
      
  