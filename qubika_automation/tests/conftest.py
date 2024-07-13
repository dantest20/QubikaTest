import pytest
from playwright.sync_api import sync_playwright
from client.club_admin_client import ClubAdminClient
from config.settings import settings


@pytest.fixture(scope="session")
def club_admin_client():
    """
    Fixture to provide a ClubAdminClient instance.

    Returns:
        ClubAdminClient: An instance of the ClubAdminClient.
    """
    return ClubAdminClient()


@pytest.fixture(scope="session")
def playwright():
    """
    Fixture to manage the Playwright instance.

    Yields:
        sync_playwright: A Playwright instance.
    """
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright):
    """
    Fixture to manage the browser instance.

    Args:
        playwright (sync_playwright): The Playwright instance.

    Yields:
        Browser: A Playwright browser instance.
    """
    browser = playwright.chromium.launch(headless=settings.HEADLESS)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """
    Fixture to manage the browser page instance.

    Args:
        browser (Browser): The Playwright browser instance.

    Yields:
        Page: A Playwright page instance.
    """
    page = browser.new_page()
    yield page
    page.close()
