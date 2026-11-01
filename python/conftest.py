import pytest
from config import Config

def pytest_configure(config):
    config.addinivalue_line("markers", "api: mark test as API test")
    config.addinivalue_line("markers", "ui: mark test as UI test")

@pytest.fixture(scope="session")
def api_headers() -> dict:
    return {
        "Authorization": f"Bearer {Config.API_KEY}",
        "Content-Type": "application/json"
    }

@pytest.fixture(scope="session")
def base_url() -> str:
    return Config.BASE_URL