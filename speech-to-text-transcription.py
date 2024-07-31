from dotenv import load_dotenv
import os 
from openai import OpenAI
# load environment variables from .env
load_dotenv() 

OPEN_AI_TOKEN = os.environ['OPEN_AI_TOKEN']
client = OpenAI(api_key=OPEN_AI_TOKEN)

#rb read binary
audio_file = open("03-01-02-01-02-02-01.wav", "rb")

response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

print(response.text)