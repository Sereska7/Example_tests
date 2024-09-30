import asyncio

import pytest
from httpx import AsyncClient, ASGITransport

from app.core.config import settings
from app.core.models.base import Base
from app.main import main_app
from app.core.models import User, Product
from app.core.models.db_helper import db_helper as db


@pytest.fixture(scope="session")
def event_loop():
    """Создание нового event loop для каждого теста."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def prepare_base():
    """Подготовка базы данных перед каждым тестом."""
    assert settings.MODE == "TEST"
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield


@pytest.fixture(scope="module")
async def ac():
    """Создание нового клиента AsyncClient для каждого теста."""
    async with AsyncClient(transport=ASGITransport(app=main_app), base_url="http://test") as ac:
        yield ac
