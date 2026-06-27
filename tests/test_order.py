import requests

def product(payload,app_url):
    return requests.post(f"{app_url}/order",json=payload)

def test_buy_success(app_url):
    test_data = {"username":"rocky","product_id":1}
    response = product(test_data,app_url)
    assert response.status_code == 200

def test_buy_fail(app_url):
    test_data = {"username":"jeetu","product_id":2}
    response = product(test_data,app_url)
    assert response.status_code == 400