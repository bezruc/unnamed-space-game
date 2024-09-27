from fastapi import FastAPI
from unnamed_game.game import Instance

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

@app.post("/start/{num_of_players}")
async def start_instance(num_of_players: int):
    Instance(num_of_players)

@app.post("/{player}/end_turn")
async def end_turn(player):
    Instance.get_instance().end_turn(player)
    

@app.get("/state/{player}")
async def get_state(player):
    return Instance.get_state(player=int(player))
