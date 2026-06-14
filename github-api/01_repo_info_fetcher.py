import requests
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

owner = "Venukaranam98"
repo = "llm-engineering-practice"

url = f"https://api.github.com/repos/{owner}/{repo}"

response = requests.get(url, headers=headers)

if response.status_code == 200:

    data = response.json()

    print(f"Repository Name : {data['name']}")
    print(f"Owner           : {data['owner']['login']}")
    print(f"Language        : {data['language']}")
    print(f"Stars           : {data['stargazers_count']}")
    print(f"Forks           : {data['forks_count']}")
    print(f"Open Issues     : {data['open_issues_count']}")

else:
    print("Error:", response.status_code)