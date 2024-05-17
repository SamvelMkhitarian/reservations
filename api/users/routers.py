from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from api.users.queryes import _create_user, _delete_user, _read_user, _update_user
from api.users.schemas import UserSchema
from api.database import get_db

router = APIRouter()


@router.post("/users/", response_model=UserSchema)
async def create_user(user: UserSchema, db: AsyncSession = Depends(get_db)):
    return await _create_user(user, db)


@router.get("/users/{user_id}", response_model=UserSchema)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await _read_user(user_id, db)


@router.put("/users/{user_id}", response_model=UserSchema)
async def update_user(user_id: int, user: UserSchema, db: AsyncSession = Depends(get_db)):
    return await _update_user(user_id, user, db)


@router.delete("/users/{user_id}", response_model=UserSchema)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await _delete_user(user_id, db)
