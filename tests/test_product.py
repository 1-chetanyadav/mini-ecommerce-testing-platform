import requests

def product(payload,app_url):
    return requests.post(f"{app_url}/products",json=payload)


def test_get_product(app_url):
    test_data = {"product_id":2}
    # print(test_data,app_url)
    response = product(test_data,app_url)
    # print(response)
    assert response.status_code == 200

def test_invalid_product(app_url):
    test_data = {"product_id":3}
    response = product(test_data,app_url)
    assert response.status_code == 400

def test_count_product(app_url):
    test_data = {"product_id":2}
    response = product(test_data,app_url)
    assert response.status_code == 200

