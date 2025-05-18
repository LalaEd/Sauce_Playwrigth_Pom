from sauce_demo.src.pages.ProductsPage import ProductsPage


class SigninPage:
    def __init__(self, page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_button = page.locator("//input[@id='login-button']")
        self._login_error_message = page.locator("//h3[@data-test='error']")

    def enter_username(self, user_name):
        self._username.clear()
        self._username.fill(user_name)

    def enter_password(self, password):
        self._password.clear()
        self._password.fill(password)

    def click_on_login_button(self):
        self._login_button.click()

    def complete_login(self, credentials):
        self.enter_username(credentials["username"])
        self.enter_password(credentials["password"])
        self.click_on_login_button()
        return ProductsPage(self.page)

    @property
    def login_error_msg(self):
        return self._login_error_message
