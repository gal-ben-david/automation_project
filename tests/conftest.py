import pytest
from playwright.sync_api import sync_playwright
from config.env import HEADLESS, BROWSER
from config.env import BASE_URL, LOCALE

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser_type = {
            "chromium": p.chromium,
            "firefox": p.firefox,
            "webkit": p.webkit,
        }[BROWSER]

        browser = browser_type.launch(headless=HEADLESS)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context(locale=LOCALE)
    page = context.new_page()
    # page.set_default_timeout(TIMEOUT)
    page.goto(BASE_URL)
    yield page
    context.close()

