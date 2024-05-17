from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from api.cancellations.queryes import _create_cancellation, _delete_cancellation, _read_cancellation
from api.cancellations.schemas import CancellationSchema
from api.database import get_db

router = APIRouter()


@router.post("/cancellations/", response_model=CancellationSchema)
async def create_cancellation(cancellation: CancellationSchema, db: AsyncSession = Depends(get_db)):
    return await _create_cancellation(cancellation, db)


@router.get("/cancellations/{cancellation_id}", response_model=CancellationSchema)
async def read_cancellation(cancellation_id: int, db: AsyncSession = Depends(get_db)):
    return await _read_cancellation(cancellation_id, db)


@router.delete("/cancellations/{cancellation_id}", response_model=CancellationSchema)
async def delete_cancellation(cancellation_id: int, db: AsyncSession = Depends(get_db)):
    return await _delete_cancellation(cancellation_id, db)
