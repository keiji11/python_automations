import os
from time import sleep
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API") 
parser.add_argument("file_name", help="The file name to save the output to") 
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key,
}

request_data = {
    "model": "text-davinci-003",
    "prompt": f"Write a script in python to {args.prompt}",
    "max_tokens": 100,
    "temperature": 0.5,
}

response = requests.post(
    api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name, "w") as f:
        f.write(response_text.strip())
else:
    print(f"Request failed with status code: {response.status_code}")
