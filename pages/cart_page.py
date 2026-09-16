from playwright.sync_api import expect


class CartPage:

    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.cart_list = page.locator(".cart_list")
        self.checkout_button = page.locator('[data-test="checkout"]')

    def get_cart_item_count(self):

        # Wait for cart page to load
        self.page.wait_for_load_state("domcontentloaded")

        print("\n========== CART DEBUG ==========")
        print("URL:", self.page.url)
        print("TITLE:", self.page.title())

        print("\n--- Cart list count ---")
        print("cart_list:", self.cart_list.count())

        print("\n--- Cart item count ---")
        print("cart_items:", self.cart_items.count())

        print("\n--- Visible page text ---")
        print(self.page.locator("body").inner_text())

        print("\n--- Cart HTML ---")
        print(self.page.locator("body").inner_html())

        print("========== END CART DEBUG ==========\n")

        return self.cart_items.count()

    def checkout(self):
        expect(self.checkout_button).to_be_visible(timeout=10000)
        self.checkout_button.click()