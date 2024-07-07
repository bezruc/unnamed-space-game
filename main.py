import logging
import sys

from fastapi import FastAPI
from unnamed_game import game_instance

app = FastAPI()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter("%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s")
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)

logger.info('API is starting up')


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

@app.get("/start")
async def start_instance():
    game_instance.init()