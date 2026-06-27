import requests
import json

def login(payload,app_url):

    return requests.post(f"{app_url}/login",json=payload)

def test_empty_username(app_url):
    test_data = {
        "username":"",
        "password":"rocky123"
        }
    response = login(test_data,app_url)
    assert response.status_code == 400

def test_empty_password(app_url):
    test_data = {
        "username":"rocky",
        "password":""
        }
    response = login(test_data,app_url)
    assert response.status_code == 400


def test_invalid_username(app_url):
    test_data = {
        "username":"rrocky",
        "password":"rocky123"
    }
    response = login(test_data,app_url)
    assert response.status_code == 401

def test_invalid_password(app_url):
    
    test_data = {
        "username":"rocky",
        "password":"rrocky123"
    }
    response = login(test_data,app_url)
    assert response.status_code == 401

def test_invalid_user_pass(app_url):
    
    test_data = {
        "username":"rrocky",
        "password":"rrocky123"
    }
    response = login(test_data,app_url)
    assert response.status_code == 401

def test_valid_user_pass(app_url):
    

    test_data = {
        "username":"rocky",
        "password":"rocky123"
    }
    response = login(test_data,app_url)
    assert response.status_code == 200
