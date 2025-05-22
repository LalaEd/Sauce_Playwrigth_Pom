from sauce_demo.src.pages.ProductsPage import ProductsPage
from typing import Any, Dict


class SigninPage:
    """Page object for the Sauce Demo sign-in page."""
    def __init__(self, page: Any) -> None:
        """Initialize the SigninPage with a Playwright page object."""
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_button = page.locator("//input[@id='login-button']")
        self._login_error_message = page.locator("//h3[@data-test='error']")

    def enter_username(self, user_name: str) -> None:
        """Enter the username in the login form."""
        self._username.clear()
        self._username.fill(user_name)

    def enter_password(self, password: str) -> None:
        """Enter the password in the login form."""
        self._password.clear()
        self._password.fill(password)

    def click_on_login_button(self) -> None:
        """Click the login button."""
        self._login_button.click()

    def complete_login(self, credentials: Dict[str, str]) -> 'ProductsPage':
        """Complete the login process and return the ProductsPage object."""
        self.enter_username(credentials["username"])
        self.enter_password(credentials["password"])
        self.click_on_login_button()
        return ProductsPage(self.page)

    @property
    def login_error_msg(self) -> Any:
        """Return the login error message locator."""
        return self._login_error_message
