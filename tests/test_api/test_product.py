import requests
import pytest
from utilities.api_helper import product_request



@pytest.mark.parametrize(
    "product_id,status_code",[(2,200),(3,400),(2,200)]
)


def test_product(app_url,product_id,status_code):
    test_data = {"product_id":product_id}
    print(test_data,app_url)
    response = product_request(test_data,app_url)
    print(response)
    assert response.status_code == status_code



