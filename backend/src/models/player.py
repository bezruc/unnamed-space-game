from pydantic import BaseModel

from .session import SessionPublic

class PlayerCreation(BaseModel):
    name: str
    email: str
    password: str
    
    
class PlayerUpdate(BaseModel):
    name: str | None
    email: str | None
    password: str | None
    
    
class PlayerPublic(BaseModel):
    id: int
    name: str
    sessions: list[SessionPublic]
    

class PlayerDB(PlayerCreation):
    hashed_password: str