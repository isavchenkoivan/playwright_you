from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.goto("https://whatsmyuseragent.org/")
#     page.screenshot(path="demo.png")
#     browser.close()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://whatsmyuseragent.org/")
    page.screenshot(path="demo1.png")
    browser.close()