import json
import os
import random
import requests


def create_page(data):
    # Initialisation
    token = os.getenv("API")
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2022-02-22"
    }
    create_url = 'https://api.notion.com/v1/pages'

    data = json.dumps(data)
    res = requests.request("POST", create_url, headers=headers, data=data)
    print(res.status_code)


if __name__ == "__main__":
    # Load the compressed data from the JSON file
    with open('notion_data.json', 'r') as json_file:
        notion_data = json.load(json_file)

    # Randomly select one entry
    random_entry = random.choice(notion_data)

    # Print the randomly selected entry
    print("Randomly Selected Entry:")
    print(random_entry)
    for item in random_entry:
        create_page(item)
