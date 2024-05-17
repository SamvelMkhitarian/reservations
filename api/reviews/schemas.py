from datetime import date
from typing import Optional
from pydantic import Field
from api.schemas import BaseSchema


class ReviewSchema(BaseSchema):
    id: int
    user_id: int
    property_id: int
    rating: int = Field(..., ge=1, le=10)
    comment: Optional[str]
    date_posted: date


class ReadReviewSchema(BaseSchema):
    user_id: int
    property_id: int
    rating: int = Field(..., ge=1, le=10)
    comment: Optional[str]
    date_posted: date
