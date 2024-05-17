from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from sqlalchemy import select

from api.database import get_db
from api.models import User


async def _create_user(user: User, db: AsyncSession = Depends(get_db)):
    stmt = User(**user.dict())
    await db.add(stmt)
    await db.commit()
    return stmt


async def _read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.id == user_id)
    if stmt is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    res = await db.execute(stmt)
    return res.scalar()


async def _update_user(user_id: int, user: User, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.id == user_id)
    if stmt is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    for key, value in user.dict().items():
        setattr(stmt, key, value)
    await db.commit()
    await db.refresh(stmt)
    return stmt


async def _delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.id == user_id)
    if stmt is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    await db.delete(stmt)
    await db.commit()
    return stmt
