from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.payments.queryes import _create_payment, _delete_payment, _read_payment
from api.payments.schemas import PaymentSchema
from api.database import get_db

router = APIRouter()


@router.post("/payments/", response_model=PaymentSchema)
async def create_payment(payment: PaymentSchema, db: AsyncSession = Depends(get_db)):
    return await _create_payment(payment, db)


@router.get("/payments/{payment_id}", response_model=PaymentSchema)
async def read_payment(payment_id: int, db: AsyncSession = Depends(get_db)):
    return await _read_payment(payment_id, db)


@router.delete("/payments/{payment_id}", response_model=PaymentSchema)
async def delete_payment(payment_id: int, db: AsyncSession = Depends(get_db)):
    return await _delete_payment(payment_id, db)
