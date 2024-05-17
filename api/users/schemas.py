from api.schemas import BaseSchema


class UserSchema(BaseSchema):
    id: int
    name: str
    surname: str
    username: str
    email: str
