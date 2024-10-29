from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from typing import Annotated

from backend.config import sqlite_url
from backend.src.tables.base import Base


connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)
Session = sessionmaker(engine)

def create_db_and_tables():
   engine = create_engine(sqlite_url)
   Base.metadata.create_all(engine)


def get_session():
    with Session() as session:
        yield session
   
     
SessionDep = Annotated[Session, Depends(get_session)]