from contextlib import asynccontextmanager
from fastapi import FastAPI

from backend.src.utils.db import create_db_and_tables
from backend.src.routers import session
from backend.src.routers import player


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(session.router)
app.include_router(player.router)