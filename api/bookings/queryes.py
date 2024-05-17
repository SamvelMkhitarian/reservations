from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from api.bookings.schemas import BookingSchema
from api.models import Booking


async def _create_booking(booking: BookingSchema, db: AsyncSession):
    stmt = Booking(**booking.model_dump())
    await db.add(stmt)
    await db.commit()
    await db.refresh(stmt)
    return stmt


async def _read_booking(booking_id: int, db: AsyncSession):
    stmt = await select(Booking).where(Booking.id == booking_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return result


async def _update_booking(booking_id: int, booking: BookingSchema, db: AsyncSession):
    stmt = await select(Booking).where(Booking.id == booking_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    for key, value in booking.items():
        setattr(result, key, value)
    await db.commit()
    await db.refresh(result)
    return result


async def _delete_booking(booking_id: int, db: AsyncSession):
    stmt = await select(Booking).where(Booking.id == booking_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    await db.delete(result)
    await db.commit()
    return result
