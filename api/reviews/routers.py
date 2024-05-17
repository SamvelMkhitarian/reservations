from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession as Session
from api.database import get_db
from api.reviews.queryes import _create_review, _delete_review, _read_review, _update_review
from api.reviews.schemas import ReadReviewSchema, ReviewSchema

router = APIRouter()


@router.post("/reviews/", response_model=ReviewSchema)
async def create_review(review: ReviewSchema, db: Session = Depends(get_db)):
    return await _create_review(review, db)


@router.get("/reviews/{review_id}", response_model=ReadReviewSchema)
async def read_review(review_id: int, db: Session = Depends(get_db)):
    return await _read_review(review_id, db)


@router.put("/reviews/{review_id}", response_model=ReadReviewSchema)
async def update_review(review_id: int, review: ReadReviewSchema, db: Session = Depends(get_db)):
    return await _update_review(review_id, review, db)


@router.delete("/reviews/{review_id}", response_model=ReadReviewSchema)
async def delete_review(review_id: int, db: Session = Depends(get_db)):
    return await _delete_review(review_id, db)
