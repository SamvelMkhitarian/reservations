from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from api.cancellations.schemas import CancellationSchema
from api.models import Cancellation


async def _create_cancellation(cancellation: CancellationSchema, db: AsyncSession):
    stmt = Cancellation(**cancellation.model_dump())
    await db.add(stmt)
    await db.commit()
    return stmt


async def _read_cancellation(cancellation_id: int, db: AsyncSession):
    stmt = await select(Cancellation).where(Cancellation.id == cancellation_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Cancellation not found")
    return result


async def _delete_cancellation(cancellation_id: int, db: AsyncSession):
    stmt = await select(Cancellation).where(Cancellation.id == cancellation_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Cancellation not found")
    await db.delete(result)
    await db.commit()
    return result
