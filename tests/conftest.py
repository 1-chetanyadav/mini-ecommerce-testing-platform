import pytest

@pytest.fixture

def app_url():
    return "http://127.0.0.1:5000"
@pytest.fixture
def valid_user():
    return {"username":"rocky","password":"rocky123"}