import requests

def product(payload):
    return requests.post("http://127.0.0.1:5000/products",json=payload)


def test_get_product():
    test_data = {"product_id":2}
    # print(test_data)
    response = product(test_data)
    # print(response)
    assert response.status_code == 200
test_get_product()

def test_invalid_product():
    test_data = {"product_id":3}
    response = product(test_data)
    assert response.status_code == 400
test_invalid_product()

def test_count_product():
    test_data = {"product_id":2}
    response = product(test_data)
    assert response.status_code == 200
test_count_product()

