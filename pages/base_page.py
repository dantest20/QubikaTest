from playwright.sync_api import Page


class BasePage:
    """
    Base page class providing common functionality for page objects.
    """

    # Menu locators
    CATEGORY_PAGE_BTN = 'text=Tipos de Categorias'

    def __init__(self, page: Page):
        """
        Initialize the BasePage with a Playwright Page object.

        Args:
            page (Page): The Playwright Page object.
        """
        self.page = page

    def go_to(self, url: str):
        """
        Navigate to a specified URL.

        Args:
            url (str): The URL to navigate to.
        """
        self.page.goto(url)

    def go_to_category_page(self):
        """
        Navigate to the category page by clicking the category page button.
        """
        btn = self.page.locator(self.CATEGORY_PAGE_BTN)
        btn.wait_for()
        btn.click()
