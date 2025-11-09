import time

import pytest
from pages.clothing_page import ClothingPage
from pages.shopping_bag_page import ShoppingBagPage

# Check console errors and status code
def test_clothing_console_errors(page, base_url):
    clothing = ClothingPage(page, base_url)
    errors = clothing.get_console_errors()
    response = clothing.open_clothing_page()

    # Assert no console errors
    assert not errors, f"Console errors found: {errors}"

    # Assert status code 200–399
    status = clothing.get_status_code(response)
    assert status is not None, "No response returned"
    assert 200 <= status < 400, f"Unexpected status code: {status}"
    assert not (400 <= status < 500), f"Client error: status {status}"


# Check products visibility on clothing page
def test_clothing_products_visibility(page, base_url):
    clothing = ClothingPage(page, base_url)
    clothing.open_clothing_page()

    # Assert products exist
    product_count = clothing.get_product_count()
    assert product_count > 0, "No products found on clothing page"

    for i in range(product_count):
        # Assert product image
        src = clothing.get_image_src(i)
        assert src, f"Product {i} image src missing"

        # Assert product title
        title = clothing.get_product_title(i)
        assert title, f"Product {i} title missing"

        # Assert product price
        price = clothing.get_product_price(i)
        assert price is not None, f"Product {i} price invalid"

        # Assert Add button visibility
        assert clothing.is_add_button_visible(i), f"Add button for product {i} not visible"


# Add product to cart and verify in shopping bag
def test_add_to_cart_and_verify(page, base_url):
    clothing = ClothingPage(page, base_url)
    bag = ShoppingBagPage(page, base_url)

    # Open clothing page
    clothing.open_clothing_page()

    product_index = 0
    product_name = clothing.get_product_title(product_index)
    product_price = clothing.get_product_price(product_index)

    # Click Add to Cart and wait for popup
    clothing.click_add_button(product_index)

    # Open shopping bag page
    bag.open_shopping_bag()

    # Assert cart has items
    count = bag.get_cart_item_count()
    assert count == 1, f"Expected 1 item in shopping bag, but found {count}"

    # Assert first item name and price
    first_item_name = bag.get_cart_item_name(0)
    first_item_price = bag.get_cart_item_price(0)

    assert first_item_name == product_name, f"Cart item name mismatch: {first_item_name} != {product_name}"
    assert first_item_price == product_price, f"Cart item price mismatch: {first_item_price} != {product_price}"