from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from api.images.schemas import ImageSchema
from api.models import Image


async def _create_image(image: ImageSchema, db: AsyncSession):
    stmt = Image(**image.model_dump())
    db.add(stmt)
    await db.commit()
    await db.refresh(stmt)
    return stmt


async def _read_image(image_id: int, db: AsyncSession):
    stmt = await select(Image).where(Image.id == image_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return result


async def _delete_image(image_id: int, db: AsyncSession):
    stmt = await db.execute(select(Image).where(Image.id == image_id))
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Image not found")
    await db.delete(result)
    await db.commit()
    return result
