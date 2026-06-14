from database import SessionLocal
from models import Event

db = SessionLocal()

events = db.query(Event).all()

print("\nAll Events\n")

for event in events:

    print("-" * 40)
    print("ID         :", event.id)
    print("Event      :", event.event)
    print("Repository :", event.repository)
    print("Created At :", event.created_at)