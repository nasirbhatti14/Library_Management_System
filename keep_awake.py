import asyncio
from playwright.async_api import async_playwright

APP_URL = "https://librarymanages.streamlit.app/"  # apna actual URL daalo

async def visit():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(APP_URL, wait_until="domcontentloaded", timeout=120_000)
        await page.wait_for_timeout(5000)

        wake_btn = page.get_by_role("button", name="Yes, get this app back up!")
        if await wake_btn.count() > 0:
            print("App was sleeping — clicking wake button")
            await wake_btn.click()
            await page.wait_for_timeout(60_000)
        else:
            print("App is already awake")

        await browser.close()

asyncio.run(visit())