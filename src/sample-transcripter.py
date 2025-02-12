import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv(verbose=True)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

audio_file = open("./input/G-01_sekken.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

print(transcription.text)
