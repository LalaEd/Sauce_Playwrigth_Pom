from playwright.sync_api import Page, expect
from sauce_demo.src.pages.SignInPage import SigninPage
from sauce_demo.tests.test_data.test_data import USERS, PRODUCTS


def test_complete_order(setup_tear_down) -> None:
    page = setup_tear_down
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(USERS["standard_user"])
    
    # Add item and proceed to checkout
    products_page.click_add_cart_button(PRODUCTS["onesie"]["id"])
    cart_page = products_page.click_cart_icon()
    
    # Complete checkout process
    checkout_page = (cart_page.click_checkout_button()
                    .complete_checkout_info("edin", "lala", "71300")
                    .click_continue_button()
                    .click_finish_button())
    
    expect(checkout_page.get_checkout_complete_message).to_contain_text("Checkout: Complete!")


def test_checkout_multiple_items(setup_tear_down) -> None:
    page = setup_tear_down
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(USERS["standard_user"])
    
    # Add multiple products to cart
    products_page.click_add_cart_button(PRODUCTS["backpack"]["id"])
    products_page.click_add_cart_button(PRODUCTS["bike_light"]["id"])
    cart_page = products_page.click_cart_icon()
    
    # Verify cart items before checkout
    expect(cart_page._cart_items).to_have_count(2)
    
    # Complete checkout process
    checkout_page = (cart_page.click_checkout_button()
                    .complete_checkout_info("John", "Doe", "12345")
                    .click_continue_button())
    
    
    checkout_page.click_finish_button()
    expect(checkout_page.get_checkout_complete_message).to_contain_text("Checkout: Complete!")


def test_checkout_empty_fields(setup_tear_down) -> None:
    page = setup_tear_down
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(USERS["standard_user"])
    
    # Setup cart and navigate to checkout
    products_page.click_add_cart_button(PRODUCTS["onesie"]["id"])
    checkout_page = products_page.click_cart_icon().click_checkout_button()
    
    # Test empty fields validation
    checkout_page.click_continue_button()
    expect(checkout_page.error_message).to_contain_text("Error: First Name is required")
    
    # Test partial form completion
    checkout_page.enter_first_name("John").click_continue_button()
    expect(checkout_page.error_message).to_contain_text("Error: Last Name is required")
    
    checkout_page.enter_last_name("Doe").click_continue_button()
    expect(checkout_page.error_message).to_contain_text("Error: Postal Code is required")


def test_cancel_checkout(setup_tear_down) -> None:
    page = setup_tear_down
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(USERS["standard_user"])
    
    # Add item and proceed to checkout
    products_page.click_add_cart_button(PRODUCTS["bolt_tshirt"]["id"])
    cart_page = products_page.click_cart_icon()
    
    # Fill info but cancel
    cart_page = (cart_page.click_checkout_button()
                 .complete_checkout_info("John", "Doe", "12345")
                 .click_cancel())
    
    # Verify return to cart
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart_page.cart_title).to_have_text("Your Cart")
    expect(cart_page._cart_items).to_have_count(1)


def test_remove_items_during_checkout(setup_tear_down) -> None:
    page = setup_tear_down
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(USERS["standard_user"])
    
    # Add multiple items
    products_page.click_add_cart_button(PRODUCTS["backpack"]["id"])
    products_page.click_add_cart_button(PRODUCTS["bike_light"]["id"])
    
    # Go to cart and remove item before checkout
    cart_page = products_page.click_cart_icon()
    cart_page.remove_item(PRODUCTS["backpack"]["id"])
    
    # Proceed to checkout
    checkout_page = (cart_page.click_checkout_button()
                    .complete_checkout_info("John", "Doe", "12345")
                    .click_continue_button())
    
    # Verify total after removal
    expect(checkout_page.total_amount).to_contain_text("$10.79")
    
    checkout_page.click_finish_button()
    expect(checkout_page.get_checkout_complete_message).to_contain_text("Checkout: Complete!")


def test_checkout_performance_user(setup_tear_down) -> None:
    page = setup_tear_down
    signin_page = SigninPage(page)
    products_page = signin_page.complete_login(USERS["performance_user"])
    
    # Complete checkout process
    checkout_page = (products_page.click_add_cart_button(PRODUCTS["backpack"]["id"])
                    .click_cart_icon()
                    .click_checkout_button()
                    .complete_checkout_info("John", "Doe", "12345")
                    .click_continue_button()
                    .click_finish_button())
    
    expect(checkout_page.get_checkout_complete_message).to_contain_text("Checkout: Complete!")
