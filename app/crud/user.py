from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import User
from app.core.models.db_helper import db_helper
from app.core.schemas.user import UserCreate


async def add_user(
        user_in: UserCreate,
        session: AsyncSession
) -> Sequence[User]:
    user = User(name=user_in.name)
    session.add(user)
    await session.commit()
    return user


async def get_user_by_id(
        user_id: int,
        session: AsyncSession
):
    stml = select(User).where(User.id == user_id)
    result = await session.scalar(stml)
    return result

