from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query
from typing import Annotated

from sqlmodel import select

from backend.src.models.session import SessionModel
from backend.src.models.session import SessionPublicModel
from backend.src.models.session import SessionCreateModel
from backend.src.utils.db import SessionDep


router = APIRouter(prefix="/session", tags=["session"])


@router.post("/", response_model=SessionPublicModel)
async def create_session(session: SessionCreateModel, db_session: SessionDep):
    session_validated = SessionModel.model_validate(session)
    db_session.add(session_validated)
    db_session.commit()
    db_session.refresh(session_validated)
    return session_validated


@router.get("/", response_model=list[SessionPublicModel])
async def get_sessions(
    db_session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    sessions = db_session.exec(select(SessionModel).offset(offset).limit(limit)).all()
    return sessions


@router.get("/{session_id}",  response_model=SessionPublicModel)
async def get_session(session_id: int, db_session: SessionDep):
    session = db_session.get(SessionModel, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session


@router.delete("/{session_id}")
async def delete_session(session_id: int, db_session: SessionDep):
    session = db_session.get(SessionModel, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    db_session.delete(session)
    db_session.commit()
    return {"ok": True}

