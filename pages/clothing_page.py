from .base_page import BasePage

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

    # Navigate to clothing/products page
    def open_clothing_page(self):
        return self.goto(self.url)

    # Get total number of products
    def get_product_count(self):
        return self.products.count()

    # Get image source of product by index
    def get_image_src(self, index):
        return self.product_images.nth(index).get_attribute("src")

    # Get product title by index
    def get_product_title(self, index):
        return self.product_titles.nth(index).inner_text()

    # Get product price as float by index
    def get_product_price(self, index):
        price_text = self.product_prices.nth(index).inner_text().replace("$", "").strip()
        try:
            return float(price_text)
        except ValueError:
            return None

    # Check if Add button is visible by index
    def is_add_button_visible(self, index):
        return self.add_buttons.nth(index).is_visible()

    # Click Add button by index
    def click_add_button(self, index):
        self.add_buttons.nth(index).click()