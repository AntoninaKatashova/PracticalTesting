import pytest
from playwright.sync_api import Playwright
from utils.base import Base

USER = "admin"
PASSWORD = "password123"

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright):
    request_context = playwright.request.new_context(
        base_url="https://restful-booker.herokuapp.com"
    )
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="session")
def client(api_request_context):
    return Base(api_request_context)

@pytest.fixture(scope="session")
def token(client):
    payload = {
        "username": USER,
        "password": PASSWORD
    }
    response = client.create_token(payload)
    assert response.ok, f"Failed to create token, status={response.status}"
    data = response.json()
    return data.get("token", "")
