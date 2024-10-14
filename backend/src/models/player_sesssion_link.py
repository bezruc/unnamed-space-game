from sqlmodel import SQLModel, Field


class PlayerSessionLinkModel(SQLModel, table=True):
    player_id: int | None = Field(default=None, foreign_key="playermodel.id", primary_key=True)
    session_id: int | None = Field(default=None, foreign_key="sessionmodel.id", primary_key=True)