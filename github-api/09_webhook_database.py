from fastapi import FastAPI, Request, BackgroundTasks

from database import SessionLocal
from models import Event

app = FastAPI()


def save_event(event_name, repository):

    db = SessionLocal()

    new_event = Event(
        event=event_name,
        repository=repository
    )

    db.add(new_event)

    db.commit()

    db.close()

    print("Event Saved To Database")


@app.post("/webhook")
async def github_webhook(
    request: Request,
    background_tasks: BackgroundTasks
):

    event = request.headers.get(
        "X-GitHub-Event"
    )

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