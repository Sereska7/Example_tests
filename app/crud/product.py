from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import Product


async def get_all_product(
        session: AsyncSession
) -> Sequence[Product]:
    stml = select(Product.__table__.columns).order_by(Product.id)
    result = await session.execute(stml)
    return result.mappings().all()
