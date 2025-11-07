import pytest
from pages.shopping_bag_page import ShoppingBagPage

#  Console errors + status
@pytest.mark.order(1)
def test_shopping_bag_console_and_status(page, base_url):
    bag = ShoppingBagPage(page, base_url)
    errors = bag.get_console_errors()
    response = bag.open_shopping_bag()
    assert not errors, f"Console errors found: {errors}"
    status = bag.get_status_code(response)
    assert status is not None
    assert 200 <= status < 400
    assert not (400 <= status < 500)

# 2️⃣ Header, checkout, total price visible
@pytest.mark.order(2)
def test_shopping_bag_header_and_checkout(page, base_url):
    bag = ShoppingBagPage(page, base_url)
    bag.open_shopping_bag()
    assert bag.header.is_visible(), "Shopping bag header not visible"
    assert bag.is_checkout_visible(), "Checkout button not visible"
    assert bag.total_price.is_visible(), "Total price not visible"
