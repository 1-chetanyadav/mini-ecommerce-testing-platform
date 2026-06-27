import requests
import pytest
from utilities.api_helper import login_request



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
    response = login_request(test_data,app_url)
    assert response.status_code == status_code

def test_valid_user_pass(app_url,valid_user):

    test_data = valid_user
    response = login_request(test_data,app_url)
    assert response.status_code == 200
