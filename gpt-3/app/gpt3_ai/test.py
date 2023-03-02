from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("CHATGPT_API_KEY")

file = open("C:/Users/Skywalker/Downloads/1.mp3", "rb")
transcription = openai.Audio.transcribe("whisper-1", file)

print(transcription)