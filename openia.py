import os
import requests
import json
from dotenv import load_dotenv
from openai import OpenAI

SYSTEM_MESSAGE = "Note we are using Nvidia's cumulus Linux distribution, just describe the commands you see.   Please keep your responses short and precise."

def call_openai_gpt4(message):
    # Load environment variables from .env file
    load_dotenv()
    client = OpenAI()
    
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": SYSTEM_MESSAGE
        },
        {
        "role": "user",
        "content": message
        }
     
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    print(response.choices[0].message.content)

    return response.choices[0].message.content

if __name__ == "__main__":

    message = '''nv set qos roce enable on
            nv set qos roce mode lossless '''
    call_openai_gpt4(message)