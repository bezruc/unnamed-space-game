import enum
from typing import TYPE_CHECKING

from sqlalchemy import Column, Enum, ForeignKey, Table

from .base import Base
from .player import Player
from .session import Session


class PlayerSessionState(enum.Enum):
    joined = "joined"
    playing = "playing"
    abandoned = "abandoned"


player_session_link = Table(
    "player_session_link",
    Base.metadata,
    Column("player_id", ForeignKey(Player.id), primary_key=True, nullable=False),
    Column("session_id", ForeignKey(Session.id), primary_key=True, nullable=False),
    Column("state", Enum(PlayerSessionState), nullable=False),
)
