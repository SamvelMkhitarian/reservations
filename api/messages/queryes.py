from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from api.messages.schemas import MessageSchema
from api.models import Message


async def _create_message(message: MessageSchema, db: AsyncSession):
    stmt = Message(**message.model_dump())
    await db.add(stmt)
    await db.commit()
    await db.refresh(stmt)
    return stmt


async def _read_message(message_id: int, db: AsyncSession):
    stmt = await select(Message).where(Message.id == message_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return result


async def _delete_message(message_id: int, db: AsyncSession):
    stmt = await select(Message).where(Message.id == message_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Message not found")
    await db.delete(result)
    await db.commit()
    return result
