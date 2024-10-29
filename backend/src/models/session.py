from datetime import datetime
from pydantic import BaseModel


class SessionCreation(BaseModel):        
    id: int
    name: str
    max_players: int
    players: list
    game: str
    status: str
    created_at: datetime
    updated_at: datetime
    

class SessionUpdate(BaseModel):
    name: str | None
    max_players: int | None
    players: list | None
    status: str | None
    

class SessionPublic(BaseModel):
    id: int
    name: str
    max_players: int
    players: list
    game: str
    status: str
    created_at: datetime
    updated_at: datetime