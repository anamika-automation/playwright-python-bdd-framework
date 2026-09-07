import os


class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = page.locator('[data-test="username"]')
        self.password = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    def login(self):
        username = os.getenv("SAUCE_USERNAME")
        password = os.getenv("SAUCE_PASSWORD")

        self.username.fill(username)
        self.password.fill(password)

        self.login_button.click()

    def get_error_message(self):
        return self.error_message.inner_text()