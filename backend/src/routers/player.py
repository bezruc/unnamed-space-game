from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated

from backend.src.models.player import PlayerCreation
from backend.src.models.player import PlayerPublic
from backend.src.models.player import PlayerInDB
from backend.src.tables.player import Player
from backend.src.utils.db import Session
from backend.src.utils.db import get_session
from backend.src.utils.auth import get_current_player

from backend.src.utils.auth import get_password_hash


router = APIRouter(prefix="/player", tags=["player"])


@router.put("/", response_model=PlayerPublic)
async def create_player(player: PlayerCreation, db_session: Session = Depends(get_session)):
    player_validated = PlayerCreation.model_validate(player)
    hashed_password = get_password_hash(player_validated.password)
    player_db = Player(username=player_validated.username, email=player_validated.email, hashed_password=hashed_password)
    
    db_session.add(player_db)
    db_session.commit()
    db_session.refresh(player_db)
    return player_db


@router.get("/me/", response_model=PlayerPublic)
async def read_users_me(current_user: Annotated[PlayerPublic, Depends(get_current_player)]):
    return current_user
