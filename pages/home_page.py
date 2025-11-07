from base_page import BasePage
from urllib.parse import urljoin

class HomePage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url

    def get_header_text(self):
        """
        Returns the visible header text in the Home page header.
        """
        locator = self.page.locator("header >> text=FashionHub")
        if locator.is_visible():
            return locator.text_content().strip()
        return None  # or raise an exception if you prefer

    def get_title_text(self):
        """
        Returns the main title text if visible, otherwise None.
        """
        locator = self.page.locator("text=Welcome to FashionHub")
        if locator.is_visible():
            return locator.text_content().strip()
        return None

    def is_shop_now_visible(self):
        """Returns True if 'Shop Now' button is visible, False otherwise."""
        return self.page.locator("text=Shop Now").is_visible()

    def is_shop_now_enabled(self):
        """Returns True if 'Shop Now' button is enabled/clickable."""
        return self.page.locator("text=Shop Now").is_enabled()

    def click_shop_now(self):
        """Clicks the 'Shop Now' button and waits for navigation."""
        self.page.locator("text=Shop Now").click()
