from fastapi import FastAPI, Request, BackgroundTasks
from datetime import datetime

app = FastAPI()


def save_event(event, repository):

    with open("events.log", "a") as file:

        file.write(
            f"{datetime.now()} | "
            f"{event} | "
            f"{repository}\n"
        )

    print("Event Saved")


@app.post("/webhook")
async def github_webhook(
    request: Request,
    background_tasks: BackgroundTasks
):

    event = request.headers.get("X-GitHub-Event")

    payload = await request.json()

    repository = payload["repository"]["name"]

    background_tasks.add_task(
        save_event,
        event,
        repository
    )

    return {
        "message": "Webhook received"
    }