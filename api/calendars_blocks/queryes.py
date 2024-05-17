from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from api.calendars_blocks.schemas import CalendarBlockSchema
from api.models import CalendarBlock


async def _create_calendar_block(calendar_block: CalendarBlockSchema, db: AsyncSession):
    db_calendar_block = CalendarBlock(**calendar_block.BaseModel())
    db.add(db_calendar_block)
    await db.commit()
    await db.refresh(db_calendar_block)
    return db_calendar_block


async def _read_calendar_block(calendar_block_id: int, db: AsyncSession):
    result = await db.select(CalendarBlock).where(CalendarBlock.id == calendar_block_id)
    db_calendar_block = result.scalars().first()
    if db_calendar_block is None:
        raise HTTPException(status_code=404, detail="Calendar block not found")
    return db_calendar_block


async def _delete_calendar_block(calendar_block_id: int, db: AsyncSession):
    result = await select(CalendarBlock).where(CalendarBlock.id == calendar_block_id)
    db_calendar_block = result.scalars().first()
    if db_calendar_block is None:
        raise HTTPException(status_code=404, detail="Calendar block not found")
    await db.delete(db_calendar_block)
    await db.commit()
    return db_calendar_block
