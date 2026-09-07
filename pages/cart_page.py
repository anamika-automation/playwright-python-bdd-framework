class CartPage:

    def __init__(self, page):
        self.page = page

        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator('[data-test="checkout"]')

    def get_cart_item_count(self):
        return self.cart_items.count()

    def checkout(self):
        self.checkout_button.click()