from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from api.payments.schemas import PaymentSchema
from api.models import Payment


async def _create_payment(payment: PaymentSchema, db: AsyncSession):
    db_payment = Payment(**payment.model_dump())
    await db.add(db_payment)
    await db.commit()
    await db.refresh(db_payment)
    return db_payment


async def _read_payment(payment_id: int, db: AsyncSession):
    result = await select(Payment).where(Payment.id == payment_id)
    db_payment = result.scalars().first()
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment


async def _delete_payment(payment_id: int, db: AsyncSession):
    result = await select(Payment).where(Payment.id == payment_id)
    db_payment = result.scalars().first()
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    await db.delete(db_payment)
    await db.commit()
    return db_payment
