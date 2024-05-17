from typing import List, Optional

from api.images.schemas import ImageSchema
from api.schemas import BaseSchema


class PropertySchema(BaseSchema):
    id: int
    name: str
    description: Optional[str]
    price_per_night: int
    images: List[ImageSchema]


class CreatePropertySchema(BaseSchema):
    name: str
    description: Optional[str]
    price_per_night: int
    images: List[ImageSchema]
