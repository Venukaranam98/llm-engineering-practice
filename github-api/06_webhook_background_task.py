from fastapi import FastAPI, Request, BackgroundTasks
import time

app = FastAPI()


def process_github_event(event, repository):

    print("\nProcessing Event...")
    time.sleep(5)

    print(f"Event Processed : {event}")
    print(f"Repository      : {repository}")


@app.post("/webhook")
async def github_webhook(
    request: Request,
    background_tasks: BackgroundTasks
):

    event = request.headers.get("X-GitHub-Event")

    payload = await request.json()

    repository = payload["repository"]["name"]

    background_tasks.add_task(
        process_github_event,
        event,
        repository
    )

    return {
        "message": "Webhook received"
    }