import os
from playwright.sync_api import expect


class ProductsPage:

    def __init__(self, page):
        self.page = page

        # SauceDemo
        self.products_title = page.locator(".title")

        self.backpack_add_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )

        self.bike_light_add_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-bike-light"]'
        )

        self.bolt_tshirt_add_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]'
        )

        self.fleece_jacket_add_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-fleece-jacket"]'
        )

        self.onesie_add_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-onesie"]'
        )

        self.red_tshirt_add_button = page.locator(
            '[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]'
        )

        self.backpack_remove_button = page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        )

        self.bike_light_remove_button = page.locator(
            '[data-test="remove-sauce-labs-bike-light"]'
        )

        self.bolt_tshirt_remove_button = page.locator(
            '[data-test="remove-sauce-labs-bolt-t-shirt"]'
        )

        self.fleece_jacket_remove_button = page.locator(
            '[data-test="remove-sauce-labs-fleece-jacket"]'
        )

        self.onesie_remove_button = page.locator(
            '[data-test="remove-sauce-labs-onesie"]'
        )

        self.red_tshirt_remove_button = page.locator(
            '[data-test="remove-test.allthethings()-t-shirt-(red)"]'
        )

        self.sort_dropdown = page.locator(
            '[data-test="product-sort-container"]'
        )

        self.cart_link = page.locator(
            '[data-test="shopping-cart-link"]'
        )

        self.cart_badge = page.locator(
            '[data-test="shopping-cart-badge"]'
        )

        self.menu_button = page.locator("#react-burger-menu-btn")

        self.logout_link = page.locator("#logout_sidebar_link")

        # Sauce Labs About / Demo
        self.about_link = page.locator(
            '[data-test="about-sidebar-link"]'
        )

        self.products_button = page.get_by_role(
            "button",
            name="Products"
        )

        self.mobile_app_distribution_link = page.get_by_role(
            "link",
            name="Mobile App Distribution"
        )

        self.request_demo_link = page.get_by_role(
            "link",
            name="Request a Demo"
        )

        self.business_email = page.locator("#Business-Email")
        self.company = page.locator("#Company")
        self.use_case = page.locator("#Use-Case")
        self.comments = page.locator("#Comments")
        self.phone = page.locator("#Phone")
        self.country = page.locator("#Country")

        self.request_demo_button = page.get_by_role(
            "button",
            name="request a demo"
        )

    # -------------------------------------------------
    # SauceDemo Product Actions
    # -------------------------------------------------

    def add_backpack(self):
        self.backpack_add_button.click()

        expect(
            self.backpack_remove_button
        ).to_be_visible(timeout=10000)

    def add_bike_light(self):
        self.bike_light_add_button.click()

        expect(
            self.bike_light_remove_button
        ).to_be_visible(timeout=10000)

    def add_bolt_tshirt(self):
        self.bolt_tshirt_add_button.click()

        expect(
            self.bolt_tshirt_remove_button
        ).to_be_visible(timeout=10000)

    def add_fleece_jacket(self):
        self.fleece_jacket_add_button.click()

        expect(
            self.fleece_jacket_remove_button
        ).to_be_visible(timeout=10000)

    def add_onesie(self):
        self.onesie_add_button.click()

        expect(
            self.onesie_remove_button
        ).to_be_visible(timeout=10000)

    def add_red_tshirt(self):
        self.red_tshirt_add_button.click()

        expect(
            self.red_tshirt_remove_button
        ).to_be_visible(timeout=10000)

    def remove_backpack(self):
        self.backpack_remove_button.click()

        expect(
            self.backpack_add_button
        ).to_be_visible(timeout=10000)

    def remove_bike_light(self):
        self.bike_light_remove_button.click()

        expect(
            self.bike_light_add_button
        ).to_be_visible(timeout=10000)

    def sort_z_to_a(self):
        self.sort_dropdown.select_option("za")

    def sort_price_low_to_high(self):
        self.sort_dropdown.select_option("lohi")

    def sort_price_high_to_low(self):
        self.sort_dropdown.select_option("hilo")

    def sort_a_to_z(self):
        self.sort_dropdown.select_option("az")

    def open_cart(self):
        self.cart_link.click()

        # Wait until the actual Cart page is rendered
        expect(
            self.page.locator('[data-test="title"]')
        ).to_have_text("Your Cart", timeout=15000)

        expect(
            self.page.locator(".cart_list")
        ).to_be_visible(timeout=15000)

        # Verify the correct URL after the Cart page is rendered
        expect(self.page).to_have_url(
            f"{os.getenv('BASE_URL')}cart.html",
            timeout=10000
        )

    # -------------------------------------------------
    # SauceDemo Logout
    # -------------------------------------------------

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()

    # -------------------------------------------------
    # Sauce Labs Demo Flow
    # -------------------------------------------------

    def open_about(self):

        self.menu_button.click()
        self.about_link.click()

    def open_mobile_app_distribution(self):

        self.page.wait_for_load_state("domcontentloaded")

        # Move mouse over Products menu
        self.products_button.hover()

        # Give the hover menu a moment to appear
        self.page.wait_for_timeout(1000)

        # Verify dropdown option is visible
        expect(
            self.mobile_app_distribution_link
        ).to_be_visible(timeout=10000)

        # Click Mobile App Distribution
        self.mobile_app_distribution_link.click()

        # Verify navigation
        expect(self.page).to_have_url(
            "https://saucelabs.com/products/mobile-app-distribution"
        )

    def open_request_demo(self):

        self.request_demo_link.click()

    def fill_demo_form(self):

        self.business_email.fill(
            "testgdjufgkurgurguirgiufgd444iudgiugd@company.com"
        )

        self.company.fill(
            "test company learning"
        )

        self.use_case.select_option(
            "Visual Testing"
        )

        self.comments.fill(
            "this is just for learning. i am testing automation project."
        )

        self.phone.fill(
            "34543453"
        )

        self.country.select_option(
            "United States"
        )

    def submit_demo_request(self):

        self.request_demo_button.click()

    def return_to_saucedemo(self):

        base_url = os.getenv("BASE_URL")

        self.page.goto(base_url)

        # Login again after returning to SauceDemo
        self.page.locator(
            '[data-test="username"]'
        ).fill("standard_user")

        self.page.locator(
            '[data-test="password"]'
        ).fill("secret_sauce")

        self.page.locator(
            '[data-test="login-button"]'
        ).click()

        # Verify Products page is displayed
        expect(
            self.products_title
        ).to_be_visible(timeout=10000)