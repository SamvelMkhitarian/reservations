from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from api.amenities.schemas import AmenitySchema
from api.models import Amenity


async def _create_amenity(amenity: AmenitySchema, db: AsyncSession):
    stmt = Amenity(**amenity.model_dump())
    await db.add(stmt)
    await db.commit()
    await db.refresh(stmt)
    return stmt


async def _read_amenity(amenity_id: int, db: AsyncSession):
    stmt = await select(Amenity).where(Amenity.id == amenity_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Amenity not found")
    return result


async def _update_amenity(amenity_id: int, amenity: AmenitySchema, db: AsyncSession):
    stmt = await select(Amenity).where(Amenity.id == amenity_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Amenity not found")
    for key, value in amenity.items():
        setattr(result, key, value)
    await db.commit()
    await db.refresh(result)
    return result


async def _delete_amenity(amenity_id: int, db: AsyncSession):
    stmt = await select(Amenity).where(Amenity.id == amenity_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Amenity not found")
    await db.delete(result)
    await db.commit()
    return result
