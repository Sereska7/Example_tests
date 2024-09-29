from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.api.views_user import router as router_user
from app.api.views_product import router as router_product
from app.core.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    print("dispose engine")
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)

main_app.include_router(router_user)
main_app.include_router(router_product)


if __name__ == "__main__":
    uvicorn.run("app.main:main_app", reload=True)
