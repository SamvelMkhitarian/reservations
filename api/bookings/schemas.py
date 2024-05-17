from datetime import date

from api.schemas import BaseSchema


class BookingSchema(BaseSchema):
    id: int
    check_in_date: date
    check_out_date: date
    user_id: int
    property_id: int
