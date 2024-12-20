from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from .player import Player
from .player_session_link import player_session_link
from .session import Session
