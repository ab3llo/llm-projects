from dotenv import load_dotenv
import os 
from openai import OpenAI
# load environment variables from .env
load_dotenv() 

OPEN_AI_TOKEN = os.environ['OPEN_AI_TOKEN']
client = OpenAI(api_key=OPEN_AI_TOKEN)

#rb read binary
audio_file = open("arabaic_audio.mp3", "rb")

response = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file,
    prompt="This is a discussion with a Doctor about an eye injury")

print(response.text)