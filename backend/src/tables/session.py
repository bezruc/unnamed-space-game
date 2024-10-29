from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from typing import TYPE_CHECKING

from .base import Base
if TYPE_CHECKING:
    from .player import Player
    


class Session(Base):
    __tablename__ = 'session'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    max_players: Mapped[int] = mapped_column(Integer)
    players: Mapped[list['Player']] = relationship(secondary='player_session_link', viewonly=True)
    game: Mapped[str] = mapped_column(String(20))
    status: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
