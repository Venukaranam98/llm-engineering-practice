from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/webhook")
async def github_webhook(request: Request):

    event = request.headers.get("X-GitHub-Event")

    payload = await request.json()

    print("\n" + "=" * 50)
    print("GitHub Event:", event)

    if event == "ping":

        print("Webhook Connected Successfully!")

    elif event == "push":

        print("New Push Received!")

        print(
            "Repository:",
            payload["repository"]["name"]
        )

        print(
            "Branch:",
            payload["ref"]
        )

    elif event == "pull_request":

        print("Pull Request Event!")

        print(
            "Action:",
            payload["action"]
        )

        print(
            "PR Title:",
            payload["pull_request"]["title"]
        )

    print("=" * 50)

    return {"status": "received"}