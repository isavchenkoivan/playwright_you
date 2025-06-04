from playwright.sync_api import sync_playwright
from urllib.request import urlretrieve

pw = sync_playwright().start()
browser = pw.firefox.launch(headless=False,
                            slow_mo=2000)

page = browser.new_page()
page.goto("http://arxiv.org/search")
page.get_by_placeholder("Search term...").fill("neural network")
page.get_by_role("button").get_by_text("Search").nth(1).click()

links = page.locator(
    "xpath=//a[contains(@href, 'arxiv.org/pdf')]"
).all()
for link in links:
    url = link.get_attribute("href")
    urlretrieve(url, "data/" + url[-5:] + ".pdf")
# print(page.content())
# print(page.title())
page.screenshot(path="new_example.png")

browser.close()