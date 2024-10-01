from fastapi import FastAPI
from contextlib import asynccontextmanager

from backend.utils.coordinator import Coordinator


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.coordinator = Coordinator()
    yield
    

app = FastAPI(lifespan=lifespan)


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}


@app.get("/start_instance/{players}")
async def start_instance(players: int):
    id = app.state.coordinator.start_instance(players)
    return {"instance_id": id}


@app.get("/{instance_id}/map")
async def get_instance_map(instance_id: int):
    return {"map": app.state.coordinator.get_instance(instance_id).get_map()}


@app.get("/{instance_id}/{player_id}/end_turn")
async def end_turn(instance_id: int, player_id: int):
    app.state.coordinator.get_instance(instance_id).player_end_turn(player_id)
    return {"message": "Turn ended"}


@app.get("/{instance_id}/get_turn_counter")
async def get_turn_timer(instance_id: int):
    return {"turn_counter": app.state.coordinator.get_instance(instance_id).get_turn_counter()}