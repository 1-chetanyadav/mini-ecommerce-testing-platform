
from playwright.sync_api import Page

def ui_login_request(page,app_url,username,password):
    page.goto(f"{app_url}/login-ui")
    page.fill("#username",username)
    page.fill("#password",password)
    page.click("#login-btn")
    
def ui_product_request(page,app_url,product_id):
    # product_id = str(product_id2)
    page.goto(f"{app_url}/product-ui")
    page.fill("#product_id",str(product_id))
    page.click("#search-btn")