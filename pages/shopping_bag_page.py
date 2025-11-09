from .base_page import BasePage

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

    # Navigate to shopping bag page and wait for it to load
    def open_shopping_bag(self):
        response = self.goto(self.url)
        self.page.locator("h1", has_text="Your Shopping Cart").wait_for(state="visible", timeout=2000)
        return response

    # Get number of items in cart
    def get_cart_item_count(self):
        return self.cart_items.count()

    # Get cart item name by index
    def get_cart_item_name(self, index):
        return self.cart_items.nth(index).locator(".cart-item-info h3").inner_text()

    # Get cart item price by index
    def get_cart_item_price(self, index):
        price_text = self.cart_items.nth(index).locator(".cart-item-info p").inner_text()
        return float(price_text.replace("Price: $", "").strip())

    # Check if checkout button is visible
    def is_checkout_visible(self):
        return self.checkout_button.is_visible()

    # Get total price text
    def get_total_price(self):
        return self.total_price.inner_text()

    # Get header text
    def get_header_text(self):
        return self.header.inner_text()

    # Get all nav links text
    def get_navigation_links_text(self):
        return [link.inner_text() for link in self.nav_links]