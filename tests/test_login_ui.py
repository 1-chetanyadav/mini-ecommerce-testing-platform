from playwright.sync_api import Page

def test_login_page_loads(page:Page):
    page.goto("http://127.0.0.1:5000/login-ui")
    assert page.title() is not None




def test_valid_login(page: Page):

    page.goto("http://127.0.0.1:5000/login-ui")

    page.fill("#username", "rocky")

    page.fill("#password", "rocky123")

    page.click("#login-btn")

    assert page.locator("#message").text_content() == "Login Success"
    
    