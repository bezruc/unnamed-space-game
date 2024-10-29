from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from backend.config import sqlite_url
from backend.src.tables.base import Base

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    engine = create_engine(sqlite_url)
    Base.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
