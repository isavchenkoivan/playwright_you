from playwright.sync_api import Page
import pytest

#@pytest.mark.skip_browser("chromium")
@pytest.mark.only_browser("chromium")
def test_title(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"

def test_inventory(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."

