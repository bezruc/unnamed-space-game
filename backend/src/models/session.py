from sqlmodel import SQLModel, Field,  Relationship
from pydantic import BaseModel
from typing import TYPE_CHECKING

from .player_sesssion_link import PlayerSessionLinkModel

if TYPE_CHECKING:
    from .player import PlayerModel
    from .player import PlayerPublicModel


class SessionBaseModel(SQLModel):
    name: str = Field(index=True)
    max_players: int
    

class SessionModel(SessionBaseModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    players: list["PlayerModel"] = Relationship(back_populates="sessions", link_model=PlayerSessionLinkModel)
    


class SessionPublicModel(SessionBaseModel):
    id: int
    
    
class SessionCreateModel(SessionBaseModel):
    pass


class SessionUpdateModel(SessionBaseModel):
    name: str | None = None
    max_players: int | None = None
    owner_id: int | None = None