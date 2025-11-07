from base_page import BasePage

class AboutPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url
        self.url = f"{base_url}about.html"

        # Banner elements
        self.banner_section = page.locator(".about-banner")
        self.banner_title = page.locator(".about-banner h1")
        self.banner_text = page.locator(".about-banner p")

    # Navigate to About page
    def open_about_page(self):
        return self.goto(self.url)

    # Get banner text
    def get_banner_title(self):
        return self.banner_title.inner_text()

    def get_banner_text(self):
        return self.banner_text.inner_text()
