from fastapi import FastAPI
from unnamed_game import game

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

@app.get("/start")
async def start_instance():
    game.init(4)

@app.get("/{player}/end_turn")
async def end_turn(player):
    game.get_instance().end_turn(player)