from sqlmodel import SQLModel, Field,  Relationship
from typing import TYPE_CHECKING, List

from .player_sesssion_link import PlayerSessionLinkModel

if TYPE_CHECKING:
    from .player import PlayerModel



class SessionBaseModel(SQLModel):
    name: str = Field(index=True)
    max_players: int
    

class SessionModel(SessionBaseModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    players: List["PlayerModel"] = Relationship(back_populates="sessions", link_model=PlayerSessionLinkModel)


class SessionPublicModel(SessionBaseModel):
    id: int
    
    
class SessionCreateModel(SessionBaseModel):
    pass


class SessionUpdateModel(SessionBaseModel):
    name: str | None = None
    max_players: int | None = None
    owner_id: int | None = None