from playwright.sync_api import Page, expect
from sauce_demo.src.pages.SignInPage import SigninPage
from sauce_demo.tests.test_data.test_data import USERS, ERROR_MESSAGES
import pytest


def test_signin_with_valid_credentials(setup_tear_down) -> None:
    """Test login with valid credentials."""
    page = setup_tear_down
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(USERS["standard_user"])
    expect(products_page.product_header).to_have_text("Products")
    expect(page.locator(".inventory_item")).to_have_count(6) 
    expect(page.locator(".shopping_cart_link")).to_be_visible()  
    expect(page.locator(".inventory_item_name")).to_have_count(6)  


def test_signin_with_valid_credentials_and_logout(setup_tear_down) -> None:
    """Test login and logout flow."""
    page = setup_tear_down
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(USERS["standard_user"])
    products_page.complete_log_out()
    expect(signin_page._login_button).to_be_visible()


@pytest.mark.parametrize("username,password,error_key", [
    ("standard", "secret", "invalid_credentials"),
    ("", "secret_sauce", "username_required"),
    ("secret_sauce", "", "password_required"),
])
def test_signin_negative_cases(setup_tear_down, username, password, error_key) -> None:
    """Test negative login scenarios with parameterization."""
    page = setup_tear_down
    signin_page = SigninPage(page)
    if username:
        signin_page.enter_username(username)
    if password:
        signin_page.enter_password(password)
    signin_page.click_on_login_button()
    expect(signin_page.login_error_msg).to_contain_text(ERROR_MESSAGES[error_key])


def test_access_products_page_without_login(setup_tear_down) -> None:
    """Test access to products page without login."""
    page = setup_tear_down
    page.goto("https://www.saucedemo.com/inventory.html")
    signin_page = SigninPage(page)
    expect(signin_page.login_error_msg).to_contain_text(ERROR_MESSAGES["inventory_access"])


def test_signin_with_locked_user(setup_tear_down) -> None:
    """Test login with locked user."""
    page = setup_tear_down
    signin_page = SigninPage(page)
    signin_page.complete_login(USERS["locked_user"])
    expect(signin_page.login_error_msg).to_contain_text(ERROR_MESSAGES["locked_user"])


def test_signin_with_performance_user(setup_tear_down) -> None:
    """Test login with performance user."""
    page = setup_tear_down
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(USERS["performance_user"])
    expect(products_page.product_header).to_have_text("Products")
    expect(page.locator(".inventory_item")).to_have_count(6)
