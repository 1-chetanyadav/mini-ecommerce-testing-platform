from playwright.sync_api import Page

def test_product_page_load(page:Page):
    page.goto("http://127.0.0.1:5000/products")
    assert page.title() is not None
    
def test_get_product(page:Page,app_url):
    
    page.goto(f"{app_url}/product-ui")
    
    page.fill("#product_id","1")
    
    page.click("#search-btn")
    
    assert page.locator("#message").text_content()== "Match Found"
    
def test_count_product(page:Page,app_url):
    page.goto(f"{app_url}/product-ui")
    
    page.fill("#product_id","2")
    
    page.click("#search-btn")
    
    assert page.locator("#message").text_content()== "Match Found"
    
def test_invalid_product(page:Page,app_url):
    page.goto(f"{app_url}/product-ui")
    page.fill("#product_id","3")
    # page.fill("#name","mouse")
    page.click("#search-btn")
    assert page.locator("#message").text_content()== "No Match Found"
    

    