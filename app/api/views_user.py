from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models.db_helper import db_helper
from app.core.schemas.user import SUser, UserCreate
from app.crud.user import add_user, get_user_by_id

router = APIRouter(
    tags=["User"]
)


@router.post("/create_user")
async def create_user(
        user_in: UserCreate,
        session: Annotated[
                AsyncSession,
                Depends(db_helper.session_getter),
            ]
) -> SUser:
    user = await add_user(user_in, session)
    return user


@router.get("/user/{user_id}")
async def get_user(
        user_id: int,
        session: Annotated[
                AsyncSession,
                Depends(db_helper.session_getter),
            ],
) -> SUser:
    user = await get_user_by_id(
        user_id,
        session
    )
    return user
