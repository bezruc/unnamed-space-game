from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from typing import TYPE_CHECKING

from .base import Base
if TYPE_CHECKING:
    from .session import Session


class Player(Base):
    __tablename__ = 'player'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    sessions: Mapped[list['Session']] = relationship(secondary='player_session_link', viewonly=True)