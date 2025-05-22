"""
Test data for Sauce Demo tests
"""

# User credentials
USERS = {
    "standard_user": {"username": "standard_user", "password": "secret_sauce"},
    "locked_user": {"username": "locked_out_user", "password": "secret_sauce"},
    "problem_user": {"username": "problem_user", "password": "secret_sauce"},
    "performance_user": {"username": "performance_glitch_user", "password": "secret_sauce"}
}

# Product data
PRODUCTS = {
    "backpack": {
        "id": "sauce-labs-backpack",
        "name": "Sauce Labs Backpack",
        "price": "$29.99"
    },
    "bike_light": {
        "id": "sauce-labs-bike-light",
        "name": "Sauce Labs Bike Light",
        "price": "$9.99"
    },
    "bolt_tshirt": {
        "id": "sauce-labs-bolt-t-shirt",
        "name": "Sauce Labs Bolt T-Shirt",
        "price": "$15.99"
    },
    "onesie": {
        "id": "sauce-labs-onesie",
        "name": "Sauce Labs Onesie",
        "price": "$7.99"
    }
}

# Error messages
ERROR_MESSAGES = {
    "locked_user": "Epic sadface: Sorry, this user has been locked out",
    "invalid_credentials": "Username and password do not match any user in this service",
    "username_required": "Username is required",
    "password_required": "Password is required",
    "inventory_access": "Epic sadface: You can only access '/inventory.html' when you are logged in."
} 