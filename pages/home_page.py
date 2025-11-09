from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url

    # Get header text (e.g., 'FashionHub')
    def get_header_text(self):
        locator = self.page.locator("header h1")
        if locator.is_visible():
            return locator.inner_text().strip()
        return None

    # Get main title text (e.g., 'Welcome to FashionHub')
    def get_title_text(self):
        locator = self.page.locator(".hero-content h1")
        if locator.is_visible():
            return locator.inner_text().strip()
        return None

    # Check if 'Shop Now' button is visible
    def is_shop_now_visible(self):
        return self.page.locator(".cta-button").is_visible()

    # Check if 'Shop Now' button is enabled/clickable
    def is_shop_now_enabled(self):
        return self.page.locator(".cta-button").is_enabled()

    # Click 'Shop Now' button,wait for navigation, and return the response.
    def click_shop_now(self):
        with self.page.expect_response("**/products.html") as response_info:
            self.page.locator(".cta-button").click()
            # Wait until the new page loads
            self.page.wait_for_url("**/products.html")
        return response_info.value