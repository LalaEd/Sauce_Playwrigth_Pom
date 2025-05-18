class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self._first_name = page.locator("//input[@id='first-name']")
        self._last_name = page.locator("//input[@id='last-name']")
        self._postal_code = page.locator("//input[@id='postal-code']")
        self._continue_button = page.locator("//input[@id='continue']")
        self._finish_button = page.locator("//button[@id='finish']")
        self._checkout_complete_message = page.locator("//span[@class='title']")

    def enter_first_name(self, first_name):
        self._first_name.clear()
        self._first_name.fill(first_name)

    def enter_last_name(self, last_name):
        self._last_name.clear()
        self._last_name.fill(last_name)

    def enter_postal_code(self, postal_code):
        self._postal_code.clear()
        self._postal_code.fill(postal_code)

    def complete_checkout_info(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue_button(self):
        self._continue_button.click()

    def click_finish_button(self):
        self._finish_button.click()

    @property
    def get_checkout_complete_message(self):
        return self._checkout_complete_message
