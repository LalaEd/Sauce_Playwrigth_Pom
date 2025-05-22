from sauce_demo.src.pages.CheckOutPage import CheckoutPage
from typing import Any


class CartPage:
    """Page object for the Sauce Demo cart page."""
    def __init__(self, page: Any) -> None:
        """Initialize the CartPage with a Playwright page object."""
        self.page = page
        self._checkout_button = page.locator("//button[@id='checkout']")
        self._cart_items = page.locator(".cart_item")
        self._cart_title = page.locator("//span[@class='title']")
        self._continue_shopping_button = page.locator("//button[@id='continue-shopping']")

    def click_checkout_button(self) -> 'CheckoutPage':
        """Click the checkout button and return the CheckoutPage object."""
        try:
            self._checkout_button.click()
        except Exception as e:
            print(f"Error clicking checkout button: {e}")
        return CheckoutPage(self.page)
    
    def get_item_quantity(self, product_id: str) -> Any:
        """Return the locator for the quantity of a product in the cart."""
        return self.page.locator(f"//div[@class='cart_item'][.//div[text()='{product_id}']]//div[@class='cart_quantity']")
    
    def get_item_price(self, product_id: str) -> Any:
        """Return the locator for the price of a product in the cart."""
        return self.page.locator(f"//div[@class='cart_item'][.//div[text()='{product_id}']]//div[@class='inventory_item_price']")
    
    def remove_item(self, product_id: str) -> None:
        """Remove an item from the cart by product id."""
        try:
            self.page.locator(f"//button[@id='remove-{product_id}']").click()
        except Exception as e:
            print(f"Error removing item {product_id}: {e}")
    
    @property
    def cart_title(self) -> Any:
        """Return the cart title locator."""
        return self._cart_title
    
    async def get_item_count(self) -> int:
        """Get the number of items in the cart asynchronously."""
        return await self._cart_items.count()
    
    def click_continue_shopping(self) -> 'ProductsPage':
        """Click the continue shopping button and return the ProductsPage object."""
        self._continue_shopping_button.click()
        from sauce_demo.src.pages.ProductsPage import ProductsPage
        return ProductsPage(self.page)
