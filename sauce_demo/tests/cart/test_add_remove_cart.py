from playwright.sync_api import Page, expect
from sauce_demo.src.pages.SignInPage import SigninPage


def test_add_product_to_cart(setup_tear_down) -> None:
    page = setup_tear_down
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(credentials)
    product_id = "sauce-labs-bike-light"  # product id used for dynamic locator
    products_page.click_add_cart_button(product_id)
    expect(products_page.remove_cart_button(product_id)).to_have_text("Remove")


def test_remove_product_from_cart(setup_tear_down) -> None:
    page = setup_tear_down
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(credentials)
    product_id = "sauce-labs-bike-light"  # product id used for dynamic locator
    products_page.click_add_cart_button(product_id)
    products_page.click_remove_cart_button(product_id)
    expect(products_page.add_cart_button(product_id)).to_have_text("Add to cart")
