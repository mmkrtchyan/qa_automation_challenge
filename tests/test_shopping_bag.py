import time

import pytest
from pages.shopping_bag_page import ShoppingBagPage

# Check console errors and status code
def test_shopping_bag_console_and_status(page, base_url):
    bag = ShoppingBagPage(page, base_url)

    # Get console errors and open page
    errors = bag.get_console_errors()
    response = bag.open_shopping_bag()

    # Assert no console errors
    assert not errors, f"Console errors found: {errors}"

    # Assert status code 200–399
    status = bag.get_status_code(response)
    assert status is not None, "No response returned"
    assert 200 <= status < 400, f"Unexpected status code: {status}"
    assert not (400 <= status < 500), f"Client error: status {status}"


# Check shopping bag header, checkout button, and total price visibility
def test_shopping_bag_header_and_checkout(page, base_url):
    bag = ShoppingBagPage(page, base_url)
    bag.open_shopping_bag()

    # Assert header visible
    assert bag.header.is_visible(), "Shopping bag header not visible"

    # Assert checkout button visible
    assert bag.is_checkout_visible(), "Checkout button not visible"

    # Assert total price visible
    assert bag.total_price.is_visible(), "Total price not visible"
