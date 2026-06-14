from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()


@app.post("/webhook")
async def github_webhook(request: Request):

    event = request.headers.get("X-GitHub-Event")

    payload = await request.json()

    timestamp = datetime.now()

    print("\n" + "=" * 60)
    print(f"Time      : {timestamp}")
    print(f"Event     : {event}")

    if event == "push":

        print(
            f"Repository: {payload['repository']['name']}"
        )

        print(
            f"Branch    : {payload['ref']}"
        )

        print(
            f"Pusher    : {payload['pusher']['name']}"
        )

    print("=" * 60)

    return {"status": "received"}