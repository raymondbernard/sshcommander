import os
import json
import requests 
from dotenv import load_dotenv

SYSTEM_MESSAGE = "Note we are using Nvidia's cumulus Linux distribution, just describe the commands you see.   Please keep your responses short and precise."
URL = "https://api.nvcf.nvidia.com/v2/nvcf/pexec/functions/df2bee43-fb69-42b9-9ee5-f4eabbeaf3a8"


# call Nivida api to retrieve AI from LLaMa2 code 32b 
def callnvidia(message):
    # Load environment variables from .env file
    load_dotenv()
    api_key = os.getenv("API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "text/event-stream",
        "Content-Type": "application/json"
    }

    data = {
        "messages": [
            {
                "content": SYSTEM_MESSAGE + message,
                "role": "user"
            }
        ],
        "temperature": 0.2,
        "top_p": 0.7,
        "max_tokens": 1024,
        "stream": True
    }

    response = requests.post(URL, headers=headers, json=data, stream=True)

    complete_message = ''
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8').strip()

            # Check if the line is the end of data marker
            if decoded_line == '[DONE]':
                print("End of data stream.")
                break

            # Remove the "data: " prefix if present
            if decoded_line.startswith('data: '):
                decoded_line = decoded_line[6:]
            try:
                json_line = json.loads(decoded_line)
                for choice in json_line['choices']:
                    complete_message += choice['delta']['content']
            except json.JSONDecodeError:
                break 

    print(complete_message)
    return complete_message

if __name__ == '__main__':
    message = '''nv set qos roce enable on
            nv set qos roce mode lossless '''
    callnvidia(message)

