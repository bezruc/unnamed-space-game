from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.sql import select

from backend.src.models.player import PlayerCreation, PlayerPublic
from backend.src.tables.player import Player
from backend.src.utils.auth import get_current_player, get_password_hash
from backend.src.utils.db import Session, get_session

router = APIRouter(prefix="/player", tags=["player"])


@router.put("/", response_model=PlayerPublic)
async def create_player(
    player: PlayerCreation, db_session: Session = Depends(get_session)
):
    if db_session.execute(
        select(Player).filter_by(username=player.username)
    ).scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Username already taken")
    if db_session.execute(
        select(Player).filter_by(email=player.email)
    ).scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Email already taken")
    hashed_password = get_password_hash(player.password)
    player_db = Player(
        username=player.username, email=player.email, hashed_password=hashed_password
    )

    db_session.add(player_db)
    db_session.commit()
    db_session.refresh(player_db)
    return player_db


@router.get("/me/", response_model=PlayerPublic)
async def read_users_me(
    current_user: Annotated[PlayerPublic, Depends(get_current_player)]
):
    return current_user
