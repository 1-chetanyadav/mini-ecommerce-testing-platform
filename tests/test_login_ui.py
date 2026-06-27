from playwright.sync_api import Page

def test_login_page_loads(page:Page,app_url):
    page.goto(f"{app_url}/login-ui")
    assert page.title() is not None




def test_valid_login(page: Page,app_url):

    page.goto(f"{app_url}/login-ui")

    page.fill("#username", "rocky")

    page.fill("#password", "rocky123")

    page.click("#login-btn")

    assert page.locator("#message").text_content() == "Login Success"
    
    