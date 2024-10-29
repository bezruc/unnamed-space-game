from fastapi import APIRouter
from passlib.hash import bcrypt

from backend.src.models.player import PlayerCreation
from backend.src.models.player import PlayerPublic
from backend.src.tables.player import Player
from backend.src.utils.db import SessionDep


router = APIRouter(prefix="/player", tags=["player"])


@router.put("/", response_model=PlayerPublic)
async def create_player(player: PlayerCreation, db_session: SessionDep):
    player_validated = PlayerCreation.model_validate(player)
    
    player_validated.password = bcrypt.hash(player_validated.password)
    player_db = Player(**player_validated.model_dump())
    
    db_session.add(player_db)
    db_session.commit()
    db_session.refresh(player_db)
    return player_db


