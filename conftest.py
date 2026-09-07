import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()


@pytest.fixture
def page():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)

        context = browser.new_context()

        page = context.new_page()

        base_url = os.getenv("BASE_URL")

        page.goto(base_url)

        yield page

        context.close()
        browser.close()