from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()


def process_data():

    print("Task Started...")

    time.sleep(10)

    print("Task Completed!")


@app.get("/")
def home(background_tasks: BackgroundTasks):

    background_tasks.add_task(process_data)

    return {
        "message": "Task running in background"
    }