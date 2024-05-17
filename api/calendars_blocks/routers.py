from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from api.calendars_blocks.queryes import _create_calendar_block, _delete_calendar_block, _read_calendar_block
from api.calendars_blocks.schemas import CalendarBlockSchema
from api.database import get_db

router = APIRouter()


@router.post("/calendar_blocks/", response_model=CalendarBlockSchema)
async def create_calendar_block(calendar_block: CalendarBlockSchema, db: AsyncSession = Depends(get_db)):
    return await _create_calendar_block(calendar_block, db)


@router.get("/calendar_blocks/{calendar_block_id}", response_model=CalendarBlockSchema)
async def read_calendar_block(calendar_block_id: int, db: AsyncSession = Depends(get_db)):
    return await _read_calendar_block(calendar_block_id, db)


@router.delete("/calendar_blocks/{calendar_block_id}", response_model=CalendarBlockSchema)
async def delete_calendar_block(calendar_block_id: int, db: AsyncSession = Depends(get_db)):
    return await _delete_calendar_block(calendar_block_id, db)
