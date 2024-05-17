from datetime import date

from api.schemas import BaseSchema


class PaymentSchema(BaseSchema):
    id: int
    user_id: int
    booking_id: int
    amount: float
    payment_date: date
