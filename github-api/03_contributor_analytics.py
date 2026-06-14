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

url = f"https://api.github.com/repos/{owner}/{repo}/contributors"

response = requests.get(url, headers=headers)

if response.status_code == 200:

   contributors = response.json()

print("\nTop Contributors\n")

for contributor in contributors[:10]:

    print("-" * 50)
    print("Username      :", contributor["login"])
    print("Contributions :", contributor["contributions"])

print("\nAnalytics Summary\n")

total_contributors = len(contributors)

top_contributor = contributors[0]["login"]

top_contributions = contributors[0]["contributions"]

total_contributions = sum(
    contributor["contributions"]
    for contributor in contributors
)

average_contributions = total_contributions / total_contributors

print(f"Total Contributors     : {total_contributors}")
print(f"Top Contributor        : {top_contributor}")
print(f"Top Contributions      : {top_contributions}")
print(f"Total Contributions    : {total_contributions}")
print(f"Average Contributions  : {average_contributions:.2f}")