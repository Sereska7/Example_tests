from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.base import Base


class User(Base):

    name: Mapped[str] = mapped_column(String(30))