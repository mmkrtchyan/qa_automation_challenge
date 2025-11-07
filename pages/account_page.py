from base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url
        self.url = f"{base_url}account.html"

        # Login page elements
        self.login_container = page.locator(".login-container")
        self.login_header = page.locator("h2", has_text="Login to FashionHub")
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#loginForm input[type='submit']")
        self.error_message = page.locator("#errorMessage")
        self.signup_link = page.locator("div.login-container p:nth-of-type(4) a[href='#']")

        # After login
        self.account_page_container = page.locator(".account-page")
        self.welcome_header = page.locator(".account-page h2")
        self.logout_button = page.locator(".account-page logout-button >> shadow=button")

    # Navigation
    def open_account(self):
        return self.goto(self.url)

    # Login helpers
    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    # Post-login helpers
    def get_welcome_text(self):
        return self.welcome_header.inner_text()

    def is_logout_visible(self):
        return self.logout_button.is_visible()

    def click_logout(self):
        self.logout_button.click()

    # Error
    def get_error_text(self):
        if self.error_message.is_visible():
            return self.error_message.inner_text()
        return None

    # Sign-up
    def click_signup(self):
        self.signup_link.click()
