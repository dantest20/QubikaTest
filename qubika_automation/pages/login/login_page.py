from config.settings import Settings
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page object model for the Login Page.
    """

    # Locators
    LOGIN_TEXT = 'text=Por favor ingrese correo y contraseña'
    EMAIL_INPUT = 'input[formcontrolname="email"]'
    PASSWORD_INPUT = 'input[formcontrolname="password"]'
    SUBMIT_BTN = 'button[type="submit"]'
    PAGE_TITLE = "Qubika Club"

    def navigate(self):
        """
        Navigate to the login page.
        """
        super().go_to(f"{Settings.BASE_URL}/#/auth/login")

    def login(self, email, password):
        """
        Perform login with the provided credentials.

        Args:
            email (str): User email.
            password (str): User password.
        """
        self.page.fill(self.EMAIL_INPUT, email)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.SUBMIT_BTN)

    def is_user_logged_in(self):
        """
        Check if the user is logged in by verifying the URL.

        Returns:
            bool: True if the user is logged in, False otherwise.
        """
        url = f"{Settings.BASE_URL}/#/dashboard"
        self.page.wait_for_url(url)
        return self.page.url == url

    def is_page_displayed(self):
        """
        Check if the login page is displayed ensuring the login text is visible and the page title matches

        Returns:
            bool: True if the login page is displayed, False otherwise.
        """
        return self.page.locator(self.LOGIN_TEXT).is_visible() and self.page.title() == self.PAGE_TITLE
