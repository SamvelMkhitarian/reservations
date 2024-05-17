from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from api.properties.queryes import _create_property, _delete_property, _read_properties, _read_property, _update_property
from api.properties.schemas import PropertySchema
from api.database import get_db

router = APIRouter()


@router.post("/properties/", response_model=PropertySchema)
async def create_property(property: PropertySchema, db: AsyncSession = Depends(get_db)):
    return await _create_property(property, db)


@router.get("/properties/{property_id}", response_model=PropertySchema)
async def read_property(property_id: int, db: AsyncSession = Depends(get_db)):
    return await _read_property(property_id, db)


@router.put("/properties/{property_id}", response_model=PropertySchema)
async def update_property(property_id: int, property: PropertySchema, db: AsyncSession = Depends(get_db)):
    return await _update_property(property_id, property, db)


@router.delete("/properties/{property_id}", response_model=PropertySchema)
async def delete_property(property_id: int, db: AsyncSession = Depends(get_db)):
    return _delete_property(property_id, db)


@router.get("/properties/", response_model=List[PropertySchema])
async def read_properties(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return _read_properties(skip, limit, db)
