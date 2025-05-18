from playwright.sync_api import Page, expect
from sauce_demo.src.pages.SignInPage import SigninPage


def test_signin_with_valid_credentials(setup_tear_down) -> None:
    page = setup_tear_down
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(credentials)
    expect(products_page.product_header).to_have_text("Products")


def test_signin_with_valid_credentials_and_logout(setup_tear_down) -> None:
    page = setup_tear_down
    credentials = {"username": "standard_user", "password": "secret_sauce"}
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(credentials)
    products_page.complete_log_out()
    expect(signin_page._login_button).to_be_visible()


def test_signin_with_invalid_credentials(setup_tear_down) -> None:
    page = setup_tear_down
    signin_page = SigninPage(page)
    signin_page.enter_username("standard")
    signin_page.enter_password("secret")
    signin_page.click_on_login_button()
    expect(signin_page.login_error_msg).to_contain_text(
        "Username and password do not match any user in this service"
    )


def test_signin_without_username(setup_tear_down) -> None:
    page = setup_tear_down
    signin_page = SigninPage(page)
    signin_page.enter_password("secret_sauce")
    signin_page.click_on_login_button()
    expect(signin_page.login_error_msg).to_contain_text("Username is required")


def test_signin_without_password(setup_tear_down) -> None:
    page = setup_tear_down
    signin_page = SigninPage(page)
    signin_page.enter_username("secret_sauce")
    signin_page.click_on_login_button()
    expect(signin_page.login_error_msg).to_contain_text("Password is required")


def test_access_products_page_without_login(setup_tear_down) -> None:
    page = setup_tear_down
    signin_page = SigninPage(page)
    expect(signin_page.login_error_msg).to_contain_text(
        "Epic sadface: You can only access '/inventory.html' when you are logged in."
    )
