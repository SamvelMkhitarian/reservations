from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from api.bookings.queryes import _create_booking, _delete_booking, _read_booking, _update_booking
from api.bookings.schemas import BookingSchema
from api.database import get_db

router = APIRouter()


@router.post("/bookings/", response_model=BookingSchema)
async def create_booking(booking: BookingSchema, db: AsyncSession = Depends(get_db)):
    return await _create_booking(booking, db)


@router.get("/bookings/{booking_id}", response_model=BookingSchema)
async def read_booking(booking_id: int, db: AsyncSession = Depends(get_db)):
    return await _read_booking(booking_id, db)


@router.put("/bookings/{booking_id}", response_model=BookingSchema)
async def update_booking(booking_id: int, booking: BookingSchema, db: AsyncSession = Depends(get_db)):
    return await _update_booking(booking_id, booking, db)


@router.delete("/bookings/{booking_id}", response_model=BookingSchema)
async def delete_booking(booking_id: int, db: AsyncSession = Depends(get_db)):
    return await _delete_booking(booking_id, db)
