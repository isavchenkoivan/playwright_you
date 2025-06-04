from playwright.async_api import async_playwright
import asyncio




async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.saucedemo.com/")
        main_title = await page.title()
        print(await page.title())
        assert main_title == "Swag Labs", "Wrong title"
        await page.screenshot(path="Swag lab.png")
        await browser.close()

asyncio.run(main())