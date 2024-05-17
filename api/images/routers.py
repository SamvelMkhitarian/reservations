from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from api.images.queryes import _create_image, _delete_image, _read_image
from api.images.schemas import ImageSchema
from api.database import get_db

router = APIRouter()


@router.post("/images/", response_model=ImageSchema)
async def create_image(image: ImageSchema, db: AsyncSession = Depends(get_db)):
    return await _create_image(image, db)


@router.get("/images/{image_id}", response_model=ImageSchema)
async def read_image(image_id: int, db: AsyncSession = Depends(get_db)):
    return await _read_image(image_id, db)


@router.delete("/images/{image_id}", response_model=ImageSchema)
async def delete_image(image_id: int, db: AsyncSession = Depends(get_db)):
    return await _delete_image(image_id, db)
