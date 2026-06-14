from fastapi import FastAPI

from database import SessionLocal
from models import Event

app = FastAPI()


@app.get("/events")
def get_events():

    db = SessionLocal()

    events = db.query(Event).all()

    result = []

    for event in events:

        result.append({
            "id": event.id,
            "event": event.event,
            "repository": event.repository,
            "created_at": event.created_at
        })

    db.close()

    return result