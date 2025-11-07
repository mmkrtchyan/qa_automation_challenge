from base_page import BasePage


class ShoppingBagPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url
        self.url = f"{base_url}cart.html"

        # Header / navigation
        self.header = page.locator("header h1")
        self.nav_links = page.locator("nav a")

        # Cart section
        self.cart_section = page.locator(".cart-section")
        self.cart_items = page.locator("#cart-items .cart-item")
        self.total_price = page.locator("#total-price")
        self.checkout_button = page.locator(".cart-summary button")

    # Navigation
    def open_shopping_bag(self):
        return self.goto(self.url)

    # Helpers
    def get_cart_item_count(self):
        return self.cart_items.count()

    def get_cart_item_name(self, index):
        return self.cart_items.nth(index).locator(".cart-item-info h3").inner_text()

    def get_cart_item_price(self, index):
        price_text = self.cart_items.nth(index).locator(".cart-item-info p").inner_text()
        return float(price_text.replace("Price: $", "").strip())

    def is_checkout_visible(self):
        return self.checkout_button.is_visible()
