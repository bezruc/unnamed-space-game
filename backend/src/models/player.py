from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING, List

from .player_sesssion_link import PlayerSessionLinkModel

if TYPE_CHECKING:
    from .session import SessionModel



class PlayerBaseModel(SQLModel):
    name: str
    email: str
       
 
class PlayerModel(PlayerBaseModel, table=True):
    id: int = Field(default=None, primary_key=True)
    hashed_password: str = Field()
    
    sessions: List["SessionModel"] = Relationship(back_populates="players", link_model=PlayerSessionLinkModel)
 

class PlayerPublicModel(PlayerBaseModel):
    id: int


class PlayerCreateModel(PlayerBaseModel):
    password: str


class PlayerUpdateModel(PlayerBaseModel):
    name: str | None = None
    email: str | None = None
    password: str | None = None
