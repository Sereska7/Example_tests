from sqlalchemy import String, DECIMAL, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.base import Base


class Product(Base):

    name: Mapped[str] = mapped_column(String(30))
    price: Mapped[DECIMAL] = mapped_column(Numeric(10, 2))