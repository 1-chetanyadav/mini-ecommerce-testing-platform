import requests

def login_request(test_data,app_url):
    return requests.post(f"{app_url}/login",json=test_data)

def product_request(test_data,app_url):
    return requests.post(f"{app_url}/products",json=test_data)