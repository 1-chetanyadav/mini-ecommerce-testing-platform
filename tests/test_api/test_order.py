import requests
import pytest

def product(payload,app_url):
    return requests.post(f"{app_url}/order",json=payload)

@pytest.mark.parametrize("username,product_id,status_code",[("rocky",1,200),("jeetu",2,400)])



def test_buys(app_url,username,product_id,status_code):
    test_data = {"username":username,"product_id":product_id}
    response = product(test_data,app_url)
    assert response.status_code == status_code

