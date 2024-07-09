from fastapi import FastAPI
from unnamed_game import game_instance

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

@app.get("/start")
async def start_instance():
    game_instance.init()