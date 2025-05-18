from sauce_demo.src.pages.CheckOutPage import CheckoutPage


class CartPage:
    def __init__(self, page):
        self.page = page
        self._checkout_button = page.locator("//button[@id='checkout']")

    def click_checkout_button(self):
        self._checkout_button.click()
        return CheckoutPage(self.page)
