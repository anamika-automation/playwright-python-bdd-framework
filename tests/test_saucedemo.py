import logging
import os
import pytest

from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


logger = logging.getLogger(__name__)


# Pytest markers for showcase/classification
pytestmark = [
    pytest.mark.saucedemo,
    pytest.mark.ui,
    pytest.mark.regression
]


# Connect BDD feature file
scenarios("../features/saucedemo.feature")


@given("I am on the SauceDemo login page")
def open_login_page(page):

    logger.info("STEP: Open SauceDemo login page")

    expect(
        page.locator('[data-test="username"]')
    ).to_be_visible()

    logger.info("STEP PASSED: Login page is displayed")


@when("I login with valid credentials")
def login_with_valid_credentials(page):

    logger.info("STEP: Login with valid credentials")

    login_page = LoginPage(page)

    login_page.login()

    expect(page).to_have_url(
        f"{os.getenv('BASE_URL')}inventory.html"
    )

    logger.info("STEP PASSED: Login successful")


@when("I open the About section")
def open_about_section(page):

    logger.info("STEP: Open About section")

    products_page = ProductsPage(page)

    products_page.open_about()

    logger.info("STEP PASSED: About section opened")


@when("I navigate to Mobile App Distribution")
def navigate_to_mobile_app_distribution(page):

    logger.info("STEP: Navigate to Mobile App Distribution")

    products_page = ProductsPage(page)

    products_page.open_mobile_app_distribution()

    logger.info("STEP PASSED: Mobile App Distribution opened")


@when("I request a demo")
def request_demo(page):

    logger.info("STEP: Request a Demo")

    products_page = ProductsPage(page)

    products_page.open_request_demo()

    logger.info("STEP PASSED: Request a Demo page opened")


@when("I submit the demo request")
def submit_demo_request(page):

    logger.info("STEP: Fill and submit demo form")

    products_page = ProductsPage(page)

    products_page.fill_demo_form()

    logger.info("Demo form completed")

    products_page.submit_demo_request()

    logger.info("STEP PASSED: Demo request submitted")


@when("I return to SauceDemo")
def return_to_saucedemo(page):

    logger.info("STEP: Return to SauceDemo")

    products_page = ProductsPage(page)

    products_page.return_to_saucedemo()

    expect(page).to_have_url(
        f"{os.getenv('BASE_URL')}inventory.html"
    )

    logger.info("STEP PASSED: Returned to SauceDemo")


@when("I add products to the cart")
def add_products_to_cart(page):

    logger.info("STEP: Add products to cart")

    products_page = ProductsPage(page)

    logger.info("Trying to add Backpack")

    products_page.add_backpack()
    logger.info("Added Backpack")

    products_page.add_bike_light()
    logger.info("Added Bike Light")

    products_page.add_bolt_tshirt()
    logger.info("Added Bolt T-Shirt")

    products_page.add_fleece_jacket()
    logger.info("Added Fleece Jacket")

    products_page.add_onesie()
    logger.info("Added Onesie")

    products_page.add_red_tshirt()
    logger.info("Added Red T-Shirt")

    logger.info("STEP PASSED: Products added")


@when("I remove selected products")
def remove_selected_products(page):

    logger.info("STEP: Remove selected products")

    products_page = ProductsPage(page)

    products_page.remove_backpack()
    logger.info("Removed Backpack")

    products_page.remove_bike_light()
    logger.info("Removed Bike Light")

    logger.info("STEP PASSED: Selected products removed")


@when("I sort the products")
def sort_products(page):

    logger.info("STEP: Sort products")

    products_page = ProductsPage(page)

    products_page.sort_z_to_a()
    logger.info("Sorted: Name Z to A")

    products_page.sort_price_low_to_high()
    logger.info("Sorted: Price Low to High")

    products_page.sort_a_to_z()
    logger.info("Sorted: Name A to Z")

    products_page.sort_price_high_to_low()
    logger.info("Sorted: Price High to Low")

    logger.info("STEP PASSED: Product sorting completed")


@when("I open the cart")
def open_cart(page):

    logger.info("STEP: Open cart")

    products_page = ProductsPage(page)

    products_page.open_cart()

    cart_page = CartPage(page)

    item_count = cart_page.get_cart_item_count()

    logger.info("Cart contains %s products", item_count)

    expect(page).to_have_url(
        f"{os.getenv('BASE_URL')}cart.html"
    )

    assert item_count == 4

    logger.info("STEP PASSED: Cart opened")


@when("I complete the checkout")
def complete_checkout(page):

    logger.info("STEP: Complete checkout")

    cart_page = CartPage(page)

    cart_page.checkout()

    logger.info("Checkout page opened")

    checkout_page = CheckoutPage(page)

    checkout_page.enter_customer_information(
        "Anamika",
        "Singh",
        "560001"
    )

    logger.info("Customer information entered")

    checkout_page.continue_checkout()

    logger.info("Checkout information confirmed")

    checkout_page.finish_order()

    logger.info("Order submitted")

    confirmation = checkout_page.get_confirmation_message()

    assert confirmation == "Thank you for your order!"

    logger.info("STEP PASSED: Checkout completed")


@when("I logout")
def logout(page):

    logger.info("STEP: Logout")

    checkout_page = CheckoutPage(page)

    checkout_page.back_to_products()

    logger.info("Returned to Products page")

    products_page = ProductsPage(page)

    products_page.logout()

    logger.info("STEP PASSED: Logout clicked")


@then("I should be logged out successfully")
def verify_logout(page):

    logger.info("STEP: Verify logout")

    expect(page).to_have_url(
        os.getenv("BASE_URL")
    )

    expect(
        page.locator('[data-test="login-button"]')
    ).to_be_visible()

    logger.info("STEP PASSED: User successfully logged out")

    logger.info("========================================")
    logger.info("SAUCEDEMO TEST COMPLETED SUCCESSFULLY")
    logger.info("========================================")