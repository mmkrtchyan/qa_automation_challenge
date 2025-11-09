from .base_page import BasePage

class AccountPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url
        self.url = f"{base_url}account.html"

        # Login page elements
        self.login_container = page.locator(".login-container")
        self.login_header = page.locator(".login-container h2")  # "Login to FashionHub"
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#loginForm input[type='submit']")
        self.error_message = page.locator("#errorMessage")
        self.signup_link = page.locator(".login-container p:nth-of-type(4) a[href='#']")

        # After login elements
        self.account_page_container = page.locator(".account-page")
        self.welcome_header = page.locator(".account-page h2")
        self.logout_button = page.locator("//div//logout-button")

    # Navigate to Account page
    def open_account(self):
        return self.goto(self.url)

    # Enter username
    def enter_username(self, username):
        self.username_input.fill(username)

    # Enter password
    def enter_password(self, password):
        self.password_input.fill(password)

    # Click the login button
    def click_login(self):
        self.login_button.click()

    # Get welcome text on the account page
    def get_welcome_text(self):
        return self.welcome_header.inner_text()

    # Check if logout button is visible
    def is_logout_button_visible(self):
        return self.logout_button.is_visible()

    # Check if account page is visible
    def is_accuont_page_visible(self):
        return (self.account_page_container.is_visible())

    # Click logout button
    def click_logout(self):
        self.logout_button.click()

    # Error message
    def get_error_text(self):
        if self.error_message.is_visible():
            return self.error_message.inner_text()
        return None

    # Sign-up button
    def click_signup(self):
        self.signup_link.click()