import pytest
from fastapi.testclient import TestClient

from src.app import app, reset_activities


@pytest.fixture(autouse=True)
def reset_app_state():
    reset_activities()
    yield
    reset_activities()


@pytest.fixture
def client():
    return TestClient(app)
