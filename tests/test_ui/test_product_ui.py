from playwright.sync_api import Page
from utilities.ui_helper import ui_product_request

def test_product_page_load(page:Page,app_url):
    page.goto(app_url)
    assert page.title() is not None
    
def test_get_product(page:Page,app_url):
    
    ui_product_request(page,app_url,2)
    
    assert page.locator("text=Match Found").is_visible
    
    
def test_invalid_product(page:Page,app_url):
    ui_product_request(page,app_url,3)
    assert page.locator("#message").text_content()== "No Match Found"
    # assert page.locator("text=No Match Found").is_visible
    

    