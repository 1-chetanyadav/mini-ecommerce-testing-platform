import requests
import pytest


def login(payload,app_url):

    return requests.post(f"{app_url}/login",json=payload)


@pytest.mark.parametrize(
    "username,password,status_code",
    [
        ("","rocky123",400),
        ("rocky","",400),
        ("roky","rocky123",401),
        ("rocky","rock12",401),
        ("ocky","ocky123",401)
     ]
)


def test_invalid_login(app_url,username,password,status_code):
    test_data = {
      "username":username,
        "password":password
        }
    response = login(test_data,app_url)
    assert response.status_code == status_code

def test_valid_user_pass(app_url,valid_user):

    test_data = valid_user
    response = login(test_data,app_url)
    assert response.status_code == 200
