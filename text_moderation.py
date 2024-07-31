from dotenv import load_dotenv
import os 
from openai import OpenAI
# load environment variables from .env
load_dotenv() 

OPEN_AI_TOKEN = os.environ['OPEN_AI_TOKEN']
client = OpenAI(api_key=OPEN_AI_TOKEN)

input = "I could kill for a hamburger"

response = client.moderations.create(
    model="text-moderation-latest",
    input=input
)

print(response.model_dump)
print(response.results[0].category_scores)
print(response.results[0].categories)
print(response.results[0].flagged)