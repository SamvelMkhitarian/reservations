from api.schemas import BaseSchema


class ImageSchema(BaseSchema):
    id: int
    property_id: int
    url: str
