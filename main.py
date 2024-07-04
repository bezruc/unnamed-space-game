from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def root():
    return {"message": "Hello World"}


@app.get("/general")
async def general():
    """
    TODO:
    - Returns general game info
    """
    return "DUMMY"


@app.get("/{player}/state")
async def player_state(player):
    """
    Currently just a dummy
    TODO:
    - Returns json with:
        * info about player resources/techs/etc
        * list of planets (id, position, visibility, resources
          (visibility based), upgrades (visibility based))
        * list of visible fleets (id, position, power, destination(if any))
    """
    return "DUMMY"


@app.post("/{player}/fleet_order/{fleet_id}/{destination_id}")
async def fleet_order():
    """
    TODO:
    - Sends an order, returns aknowledgment or error
    """
    return "DUMMY"


@app.post("/{player}/planet_upgrade/{planet_id}/{type_of_upgrade}")
async def planet_upgrade():
    """
    TODO:
    - Sends an upgrade, returns aknowledgment or error
    """
    return "DUMMY"


@app.post("/{player}/research_change/{what_research}")
async def select_research():
    """
    TODO:
    - Sends an research option, returns aknowledgment or error
    """
    return "DUMMY"


@app.post("/{who}/trade/{with}/{research_or_number}")
async def trade():
    """
    TODO:
    - Sends a trade, returns aknowledgment or error
    """
    return "DUMMY"


@app.post("/{player}/end_turn")
async def end_turn():
    """
    TODO:
    - Sends an end turn, returns aknowledgment or error
    """
    return "DUMMY"
