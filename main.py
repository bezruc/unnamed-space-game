from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


"""
TODO:

GET "/{player}/state"
- Returns json with:
    * list of planets        (id, position, visibility, resources (visibility based), upgrades (visibility based))
    * list of visible fleets (id, position, power, destination(if any))

GET "/{player}/general"
- Returns json with general info:
    * other player stats
    * game options
    * research info

POST "/{player}/fleet_order/{fleet_id}/{destination_id}
- Sends an order, returns aknowledgment or error

POST "/{player}/planet_upgrade/{planet_id}/{type_of_upgrade}
- Sends an upgrade, returns aknowledgment or error

POST "/{player}/research_change/{what_research}
- Sends an research optiion, returns aknowledgment or error

POST "/{player}/trade/{player}/{research_or_number}
- Sends a trade, returns aknowledgment or error

POST "/{player}/end_turn
- Sends an end turn, returns aknowledgment or error
"""