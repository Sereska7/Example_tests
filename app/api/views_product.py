from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models.db_helper import db_helper
from app.core.schemas.product import SProduct
from app.crud.product import get_all_product

router = APIRouter(
    tags=["Product"]
)


@router.get("/get_products")
async def get_products(
        session:
        Annotated[
            AsyncSession,
            Depends(db_helper.session_getter)
        ]
) -> list[SProduct]:
    products = await get_all_product(session)
    return products

