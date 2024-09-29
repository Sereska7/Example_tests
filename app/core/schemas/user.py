from pydantic import BaseModel


class SUser(BaseModel):
    id: int
    name: str


class UserCreate(BaseModel):
    name: str
