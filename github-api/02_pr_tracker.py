import requests
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

owner = "fastapi"
repo = "fastapi"

url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

response = requests.get(url, headers=headers)

if response.status_code == 200:

    pulls = response.json()

    print(f"\nFound {len(pulls)} Pull Requests\n")

    for pr in pulls:

        print("-" * 50)
        print("PR Number  :", pr["number"])
        print("Title      :", pr["title"])
        print("Author     :", pr["user"]["login"])
        print("State      :", pr["state"])
        print("URL        :", pr["html_url"])

        print("\nAvailable Keys:")
        print(pr.keys())

        break

else:
    print("Error:", response.status_code)