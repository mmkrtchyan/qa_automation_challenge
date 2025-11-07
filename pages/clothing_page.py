from base_page import BasePage

class ClothingPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url
        self.url = f"{base_url}products.html"

        # Products section
        self.products = page.locator(".product-list .product")
        self.product_images = page.locator(".product .image-container img")
        self.product_titles = page.locator(".product h3")
        self.product_prices = page.locator(".product p:nth-of-type(2)")
        self.add_buttons = page.locator(".product button")

        # Popup
        self.popup = page.locator("#popup")
        self.popup_ok_button = self.popup.locator("button")

    # Navigation
    def open_clothing_page(self):
        return self.goto(self.url)

    # Product helpers
    def get_product_count(self):
        return self.products.count()

    def get_image_src(self, index):
        return self.product_images.nth(index).get_attribute("src")

    def get_product_title(self, index):
        return self.product_titles.nth(index).inner_text()

    def get_product_price(self, index):
        price_text = self.product_prices.nth(index).inner_text().replace("$", "").strip()
        try:
            return float(price_text)
        except ValueError:
            return None

    def is_add_button_visible(self, index):
        return self.add_buttons.nth(index).is_visible()

    def click_add_button(self, index):
        self.add_buttons.nth(index).click()

    # Popup helpers
    def wait_for_popup(self, timeout=2000):
        self.popup.wait_for(state="visible", timeout=timeout)

    def click_popup_ok(self):
        self.popup_ok_button.click()
        self.popup.wait_for(state="hidden", timeout=2000)

    def is_popup_visible(self):
        return self.popup.is_visible()
