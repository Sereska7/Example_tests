import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "name,status_code",
    [
        ("Sergey", 200),
        ("Vano", 200),
        (5767, 422)
    ]
)
async def test_create_user1(name, status_code, ac: AsyncClient):
    response = await ac.post("/create_user", json={"name": name})
    assert response.status_code == status_code


@pytest.mark.parametrize(
    "user_id,status_code",
    [
        (1, 200),
        (2, 200),
        ("f", 422)
    ]
)
async def test_get_user(user_id, status_code, ac: AsyncClient):
    response = await ac.get(f"/user/{user_id}", params={"user_id": user_id})
    assert response.status_code == status_code


@pytest.mark.asyncio
async def test_get_products(ac: AsyncClient):
    response = await ac.get("/get_products")
    assert response.status_code == 200
