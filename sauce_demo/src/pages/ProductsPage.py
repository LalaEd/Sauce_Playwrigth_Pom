from sauce_demo.src.pages.CartPage import CartPage
from typing import Any


class ProductsPage:
    """Page object for the Sauce Demo products page."""
    def __init__(self, page: Any) -> None:
        """Initialize the ProductsPage with a Playwright page object."""
        self.page = page
        self._products_header = page.locator("span.title")
        self._main_menu = page.locator("//button[normalize-space()='Open Menu']")
        self._logout_button = page.locator("//a[@id='logout_sidebar_link']")
        self._cart_icon = page.locator("//a[@class='shopping_cart_link']")

    @property
    def product_header(self) -> Any:
        """Return the products header locator."""
        return self._products_header

    def click_on_main_menu(self) -> 'ProductsPage':
        """Click the main menu button."""
        self._main_menu.click()
        return self

    def click_on_logout_button(self) -> 'ProductsPage':
        """Click the logout button."""
        self._logout_button.click()
        return self

    def complete_log_out(self) -> 'ProductsPage':
        """Complete the logout process and return self."""
        self.click_on_main_menu()
        self.click_on_logout_button()
        return self

    def add_cart_button(self, product_id: str) -> Any:
        """Return the locator for the add to cart button for a product."""
        return self.page.locator(
            f"[data-test='add-to-cart-{product_id}']"
        )  # creating dynamic locator for all products

    def click_add_cart_button(self, product_id: str) -> 'ProductsPage':
        """Click the add to cart button for a product."""
        self.add_cart_button(product_id).click()
        return self

    def remove_cart_button(self, product_id: str) -> Any:
        """Return the locator for the remove from cart button for a product."""
        return self.page.locator(
            f"[data-test='remove-{product_id}']"
        )  # creating dynamic locator for all products

    def click_remove_cart_button(self, product_id: str) -> 'ProductsPage':
        """Click the remove from cart button for a product."""
        self.remove_cart_button(product_id).click()
        return self

    def click_cart_icon(self) -> 'CartPage':
        """Click the cart icon and return the CartPage object."""
        self._cart_icon.click()
        return CartPage(self.page)
