from typing import Any

class CheckoutPage:
    """Page object for the Sauce Demo checkout page."""
    def __init__(self, page: Any) -> None:
        """Initialize the CheckoutPage with a Playwright page object."""
        assert page is not None, "Page object must not be None"
        self.page = page
        # Form fields
        self._first_name = page.locator("//input[@id='first-name']")
        self._last_name = page.locator("//input[@id='last-name']")
        self._postal_code = page.locator("//input[@id='postal-code']")
        
        # Buttons
        self._continue_button = page.locator("//input[@id='continue']")
        self._finish_button = page.locator("//button[@id='finish']")
        self._cancel_button = page.locator("#cancel")
        
        # Messages and info
        self._checkout_complete_message = page.locator("//span[@class='title']")
        self._error_message = page.locator("[data-test='error']")
        self._total_price = page.locator(".summary_total_label")
        self._subtotal = page.locator(".summary_subtotal_label")
        self._tax = page.locator(".summary_tax_label")

    # Form field methods
    def enter_first_name(self, first_name: str) -> 'CheckoutPage':
        """Enter the first name in the checkout form."""
        self._first_name.clear()
        self._first_name.fill(first_name)
        return self

    def enter_last_name(self, last_name: str) -> 'CheckoutPage':
        """Enter the last name in the checkout form."""
        self._last_name.clear()
        self._last_name.fill(last_name)
        return self

    def enter_postal_code(self, postal_code: str) -> 'CheckoutPage':
        """Enter the postal code in the checkout form."""
        self._postal_code.clear()
        self._postal_code.fill(postal_code)
        return self

    def complete_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> 'CheckoutPage':
        """Fill in all checkout info fields."""
        return (self.enter_first_name(first_name)
                .enter_last_name(last_name)
                .enter_postal_code(postal_code))

    # Button actions
    def click_continue_button(self) -> 'CheckoutPage':
        """Click the continue button."""
        try:
            self._continue_button.click()
        except Exception as e:
            print(f"Error clicking continue button: {e}")
        return self

    def click_finish_button(self) -> 'CheckoutPage':
        """Click the finish button."""
        try:
            self._finish_button.click()
        except Exception as e:
            print(f"Error clicking finish button: {e}")
        return self

    def click_cancel(self) -> 'CartPage':
        """Click the cancel button and return the CartPage object."""
        try:
            self._cancel_button.click()
        except Exception as e:
            print(f"Error clicking cancel button: {e}")
        from sauce_demo.src.pages.CartPage import CartPage
        return CartPage(self.page)

    # Item management
    def get_item_price(self, product_name: str) -> Any:
        """Return the locator for the price of a product in the checkout page."""
        return self.page.locator(f"//div[text()='{product_name}']/following-sibling::div[@class='item_pricebar']//div[@class='inventory_item_price']")

    def remove_item_button(self, product_id: str) -> Any:
        """Return the locator for the remove button of a product."""
        return self.page.locator(f"//button[@id='remove-{product_id}']")

    def remove_item(self, product_id: str) -> 'CheckoutPage':
        """Remove an item from the checkout page by product id."""
        try:
            button = self.remove_item_button(product_id)
            button.wait_for(state="visible")
            button.click()
        except Exception as e:
            print(f"Error removing item {product_id}: {e}")
        return self

    # Information getters
    @property
    def get_checkout_complete_message(self) -> Any:
        """Return the checkout complete message locator."""
        return self._checkout_complete_message

    @property
    def error_message(self) -> Any:
        """Return the error message locator."""
        return self._error_message

    @property
    def total_amount(self) -> Any:
        """Return the total amount locator."""
        return self._total_price

    @property
    def subtotal_amount(self) -> Any:
        """Return the subtotal amount locator."""
        return self._subtotal

    @property
    def tax_amount(self) -> Any:
        """Return the tax amount locator."""
        return self._tax
