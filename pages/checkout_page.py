class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')

        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')

        self.complete_header = page.locator('[data-test="complete-header"]')

        self.back_home_button = page.locator('[data-test="back-to-products"]')


    def enter_customer_information(self, first_name, last_name, postal_code):

        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)


    def continue_checkout(self):

        self.continue_button.click()


    def finish_order(self):

        self.finish_button.click()


    def get_confirmation_message(self):

        return self.complete_header.inner_text()


    def back_to_products(self):

        self.back_home_button.click()