from playwright.sync_api import Page
from utilities.ui_helper import ui_login_request

def test_login_page_loads(page:Page,app_url):
    page.goto(f"{app_url}/login-ui")
    assert page.title() is not None



def test_valid_login(page: Page,app_url):

    ui_login_request(page,app_url,"rocky","rocky123")
    assert page.locator("#message").text_content() == "Login Success"
    
    