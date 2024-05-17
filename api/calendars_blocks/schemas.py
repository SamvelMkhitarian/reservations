from datetime import date

from api.schemas import BaseSchema


class CalendarBlockSchema(BaseSchema):
    id: int
    property_id: int
    start_date: date
    end_date: date
