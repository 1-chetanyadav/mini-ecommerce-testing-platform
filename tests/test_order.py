import requests

def product(payload):
    return requests.post("http://127.0.0.1:5000/order",json=payload)

def test_buy_success():
    test_data = {"username":"rocky","product_id":1}
    response = product(test_data)
    assert response.status_code == 200
test_buy_success()

def test_buy_fail():
    test_data = {"username":"jeetu","product_id":2}
    response = product(test_data)
    assert response.status_code == 400
test_buy_fail()