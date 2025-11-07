import pytest
from pages.clothing_page import ClothingPage

@pytest.mark.order(1)
def test_clothing_console_errors(page, base_url):
    clothing = ClothingPage(page, base_url)
    errors = clothing.get_console_errors()
    response = clothing.open_clothing_page()

    # Console errors
    assert not errors, f"Console errors found: {errors}"

    # Status code
    status = clothing.get_status_code(response)
    assert status is not None, "No response returned"
    assert 200 <= status < 400, f"Unexpected status code: {status}"
    assert not (400 <= status < 500), f"Client error: status {status}"


@pytest.mark.order(2)
def test_clothing_products_visibility(page, base_url):
    clothing = ClothingPage(page, base_url)
    clothing.open_clothing_page()

    product_count = clothing.get_product_count()
    assert product_count > 0, "No products found on clothing page"

    for i in range(product_count):
        src = clothing.get_image_src(i)
        assert src, f"Product {i} image src missing"

        title = clothing.get_product_title(i)
        assert title, f"Product {i} title missing"

        price = clothing.get_product_price(i)
        assert price is not None, f"Product {i} price invalid: {clothing.product_prices.nth(i).inner_text()}"

        assert clothing.is_add_button_visible(i), f"Add button for product {i} not visible"


@pytest.mark.order(3)
def test_add_to_cart_and_verify(page, base_url):
    clothing = ClothingPage(page, base_url)
    clothing.open_clothing_page()

    product_index = 0
    product_name = clothing.get_product_title(product_index)
    product_price = clothing.get_product_price(product_index)

    # Click Add to Cart
    clothing.click_add_button(product_index)

    # Wait for popup and assert
    clothing.wait_for_popup()
    assert clothing.is_popup_visible(), "Popup did not appear after adding to cart"

    # Click OK in popup
    clothing.click_popup_ok()
    assert not clothing.is_popup_visible(), "Popup did not close after clicking OK"

    # Open Shopping Bag
    shopping_bag_url = f"{base_url}cart.html"
    page.goto(shopping_bag_url)

    # Assert cart items exist
    cart_items = page.locator("#cart-items .cart-item")
    assert cart_items.count() > 0, "No items in shopping bag"

    # Check first item name & price
    first_item_name = cart_items.nth(0).locator(".cart-item-info h3").inner_text()
    first_item_price_text = cart_items.nth(0).locator(".cart-item-info p").inner_text()
    first_item_price = float(first_item_price_text.replace("Price: $", "").strip())

    assert first_item_name == product_name, f"Cart item name mismatch: {first_item_name} != {product_name}"
    assert first_item_price == product_price, f"Cart item price mismatch: {first_item_price} != {product_price}"
