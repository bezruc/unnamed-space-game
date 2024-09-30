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


@app.get("/get_instance/{id}/map")
async def get_instance_map(id: int):
    return app.state.coordinator.get_instance(id).get_map()