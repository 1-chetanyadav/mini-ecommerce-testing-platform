import requests
import json

def login(payload):
    #   debug
    # print("payload:",payload)
    return requests.post("http://127.0.0.1:5000/login",json=payload)


def test_invalid_username():
    test_data = {
        "username":"rrocky",
        "password":"rocky123"
    }
    response = login(test_data)
    assert response.status_code == 401
test_invalid_username()

def test_invalid_password():
    
    test_data = {
        "username":"rocky",
        "password":"rrocky123"
    }
    response = login(test_data)
    assert response.status_code==401
test_invalid_password()

def test_invalid_user_pass():
    
    test_data = {
        "username":"rrocky",
        "password":"rrocky123"
    }
    response = login(test_data)
    assert response.status_code == 401
test_invalid_user_pass()

def test_valid_user_pass():
    

    test_data = {
        "username":"rocky",
        "password":"rocky123"
    }
    response = login(test_data)
    assert response.status_code==200
test_valid_user_pass()
