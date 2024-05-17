from datetime import date

from api.schemas import BaseSchema


class MessageSchema(BaseSchema):
    id: int
    sender_id: int
    recipient_id: int
    content: str
    date_sent: date
