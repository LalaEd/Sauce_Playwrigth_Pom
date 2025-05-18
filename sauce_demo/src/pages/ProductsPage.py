from sauce_demo.src.pages.CartPage import CartPage


class ProductsPage:
    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("span.title")
        self._main_menu = page.locator("//button[normalize-space()='Open Menu']")
        self._logout_button = page.locator("//a[@id='logout_sidebar_link']")
        self._cart_icon = page.locator("//a[@class='shopping_cart_link']")

    @property
    def product_header(self):
        return self._products_header

    def click_on_main_menu(self):
        self._main_menu.click()

    def click_on_logout_button(self):
        self._logout_button.click()

    def complete_log_out(self):
        self.click_on_main_menu()
        self.click_on_logout_button()

    def add_cart_button(self, product_id):
        return self.page.locator(
            f"[data-test='add-to-cart-{product_id}']"
        )  # creating dynamic locator for all products

    def click_add_cart_button(self, product_id):
        self.add_cart_button(product_id).click()

    def remove_cart_button(self, product_id):
        return self.page.locator(
            f"[data-test='remove-{product_id}']"
        )  # creating dynamic locator for all products

    def click_remove_cart_button(self, product_id):
        self.remove_cart_button(product_id).click()

    def click_cart_icon(self):
        self._cart_icon.click()
        return CartPage(self.page)
