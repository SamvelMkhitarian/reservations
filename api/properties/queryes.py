from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from api.properties.schemas import CreatePropertySchema
from api.models import Property
from api.database import get_db

router = APIRouter()


async def _create_property(property: CreatePropertySchema, db: AsyncSession = Depends(get_db)):
    stmt = Property(**property.model_dump())
    await db.add(stmt)
    await db.commit()
    await db.refresh(stmt)
    return stmt


async def _read_property(property_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(Property).where(Property.id == property_id)
    if stmt is None:
        raise HTTPException(status_code=404, detail="Объект не найден")
    return stmt


async def _update_property(property_id: int, property: CreatePropertySchema, db: AsyncSession = Depends(get_db)):
    stmt = select(Property).where(Property.id == property_id)
    if stmt is None:
        raise HTTPException(status_code=404, detail="Объект не найден")
    for key, value in property.items():
        setattr(stmt, key, value)
    await db.commit()
    await db.refresh(stmt)
    return stmt


async def _delete_property(property_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(Property).where(Property.id == property_id)
    if stmt is None:
        raise HTTPException(status_code=404, detail="Объект не найден")
    await db.delete(stmt)
    await db.commit()
    return stmt


async def _read_properties(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    stmt = select(Property).offset(skip).limit(limit).all()
    return stmt
