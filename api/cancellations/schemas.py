from api.schemas import BaseSchema


class CancellationSchema(BaseSchema):
    id: int
    booking_id: int
    reason: str
    cancelled_by_user: bool
