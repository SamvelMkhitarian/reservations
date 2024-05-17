from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from api.messages.queryes import _create_message, _delete_message, _read_message
from api.messages.schemas import MessageSchema
from api.database import get_db

router = APIRouter()


@router.post("/messages/", response_model=MessageSchema)
async def create_message(message: MessageSchema, db: AsyncSession = Depends(get_db)):
    return await _create_message(message, db)


@router.get("/messages/{message_id}", response_model=MessageSchema)
async def read_message(message_id: int, db: AsyncSession = Depends(get_db)):
    return await _read_message(message_id, db)


@router.delete("/messages/{message_id}", response_model=MessageSchema)
async def delete_message(message_id: int, db: AsyncSession = Depends(get_db)):
    return await _delete_message(message_id, db)
