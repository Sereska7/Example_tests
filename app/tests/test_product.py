import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_products(ac: AsyncClient):
    response = await ac.get("/get_products")
    assert response.status_code == 200
