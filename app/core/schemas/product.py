from pydantic import BaseModel


class SProduct(BaseModel):
    id: int
    name: str
    price: float
