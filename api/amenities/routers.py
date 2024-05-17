from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from api.amenities.queryes import _create_amenity, _delete_amenity, _read_amenity, _update_amenity
from api.amenities.schemas import AmenitySchema
from api.database import get_db

router = APIRouter()


@router.post("/amenities/", response_model=AmenitySchema)
async def create_amenity(amenity: AmenitySchema, db: AsyncSession = Depends(get_db)):
    return await _create_amenity(amenity, db)


@router.get("/amenities/{amenity_id}", response_model=AmenitySchema)
async def read_amenity(amenity_id: int, db: AsyncSession = Depends(get_db)):
    return await _read_amenity(amenity_id, db)


@router.put("/amenities/{amenity_id}", response_model=AmenitySchema)
async def update_amenity(amenity_id: int, amenity: AmenitySchema, db: AsyncSession = Depends(get_db)):
    return await _update_amenity(amenity_id, amenity, db)


@router.delete("/amenities/{amenity_id}", response_model=AmenitySchema)
async def delete_amenity(amenity_id: int, db: AsyncSession = Depends(get_db)):
    return await _delete_amenity(amenity_id, db)
