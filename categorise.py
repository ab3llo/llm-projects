from dotenv import load_dotenv
import os 
from openai import OpenAI
# load environment variables from .env
load_dotenv() 

OPEN_AI_TOKEN = os.environ['OPEN_AI_TOKEN']
client = OpenAI(api_key=OPEN_AI_TOKEN)

prompt_text = """Specify a category for the following companies, Apple, Tesla, Microsoft, Alphabet, LVMH, Berkshire Hathaway and Saudi Aramco
Use the following categories:
1. Tech
2. Energy
3. Luxury Goods
4. Investment
"""

# This makes a request to the completions endpoint - the endpoint for completing a text
response =  client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt_text,
    max_tokens=200,
    temperature=0
)

print(response.choices[0].text)