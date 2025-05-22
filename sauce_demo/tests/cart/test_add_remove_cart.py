from playwright.sync_api import Page, expect
from sauce_demo.src.pages.SignInPage import SigninPage
from sauce_demo.tests.test_data.test_data import USERS, PRODUCTS
import pytest


@pytest.mark.parametrize("product_key", ["bike_light", "backpack", "bolt_tshirt", "onesie"])
def test_add_product_to_cart(setup_tear_down, product_key) -> None:
    """Test adding a product to the cart."""
    page = setup_tear_down
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(USERS["standard_user"])
    product_id = PRODUCTS[product_key]["id"]
    products_page.click_add_cart_button(product_id)
    expect(products_page.remove_cart_button(product_id)).to_have_text("Remove")


@pytest.mark.parametrize("product_key", ["bike_light", "backpack", "bolt_tshirt", "onesie"])
def test_remove_product_from_cart(setup_tear_down, product_key) -> None:
    """Test removing a product from the cart."""
    page = setup_tear_down
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(USERS["standard_user"])
    product_id = PRODUCTS[product_key]["id"]
    products_page.click_add_cart_button(product_id)
    products_page.click_remove_cart_button(product_id)
    expect(products_page.add_cart_button(product_id)).to_have_text("Add to cart")
