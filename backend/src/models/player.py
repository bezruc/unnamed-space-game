from pydantic import BaseModel

from .session import SessionPublic


class PlayerCreation(BaseModel):
    username: str
    email: str
    password: str
    

class PlayerInDB(BaseModel):
    username: str
    email: str
    hashed_password: str
    sessions: list[SessionPublic] | None
    

    
class PlayerUpdate(BaseModel):
    username: str | None
    email: str | None
    hashed_password: str | None
    
    
class PlayerPublic(BaseModel):
    id: int
    username: str
    sessions: list[SessionPublic]
