from playwright.sync_api import Page, expect
from sauce_demo.src.pages.SignInPage import SigninPage


def test_complete_order(setup_tear_down) -> None:
    page = setup_tear_down
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(credentials)
    product_id = "sauce-labs-onesie"  # product id used for dynamic locator
    products_page.click_add_cart_button(product_id)
    cart_page = products_page.click_cart_icon()
    checkout_page = cart_page.click_checkout_button()
    checkout_page.complete_checkout_info("edin", "lala", "71300")
    checkout_page.click_continue_button()
    checkout_page.click_finish_button()
    expect(checkout_page.get_checkout_complete_message).to_contain_text(
        "Checkout: Complete!"
    )
