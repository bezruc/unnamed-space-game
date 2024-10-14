from fastapi import APIRouter
from passlib.hash import bcrypt

from backend.src.models.player import PlayerCreateModel
from backend.src.models.player import PlayerPublicModel
from backend.src.models.player import PlayerModel
from backend.src.utils.db import SessionDep


router = APIRouter(prefix="/player", tags=["player"])


@router.put("/", response_model=PlayerPublicModel)
async def create_player(player: PlayerCreateModel, db_session: SessionDep):
    hashed_password = bcrypt.hash(player.password)
    extra_data = {"hashed_password": hashed_password}
    player_validated = PlayerModel.model_validate(player, update=extra_data)
    
    db_session.add(player_validated)
    db_session.commit()
    db_session.refresh(player_validated)
    return player_validated


