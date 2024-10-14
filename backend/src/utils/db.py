from fastapi import Depends
from typing import Annotated
from sqlmodel import SQLModel, Field, Session, create_engine

from backend.config import sqlite_url


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)
