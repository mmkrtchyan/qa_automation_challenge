from pages.home_page import HomePage

#Check console errors and status code
def test_console_errors(page, base_url):
    home = HomePage(page, base_url)

    # Collect console errors
    errors = home.get_console_errors()
    response = home.goto(base_url)  # Navigate to home page

    assert not errors, f"Console errors found: {errors}"

    # Assert status code is 200–399
    status = home.get_status_code(response)
    assert status is not None, "No response returned"
    assert 200 <= status < 400, f"Unexpected status code: {status}"
    assert not (400 <= status < 500), f"Client error: status {status}"

#Check header and main title
def test_home_screen(page, base_url):
    home = HomePage(page, base_url)
    home.goto(base_url)  # Navigate to page first

    # Assert header
    header = home.get_header_text()
    assert header == "FashionHub", f"Header text mismatch: {header}"

    # Assert main title
    title = home.get_title_text()
    assert title == "Welcome to FashionHub", f"Title text mismatch: {title}"

#Check 'Shop Now' button and navigation
def test_shop_now(page, base_url):
    home = HomePage(page, base_url)
    home.goto(base_url)

    # Assert button
    assert home.is_shop_now_visible(), "'Shop Now' button is not visible"
    assert home.is_shop_now_enabled(), "'Shop Now' button is not clickable"

    # Click and get response
    response = home.click_shop_now()

    # Check status code
    status = home.get_status_code(response)
    assert status is not None, "No response returned after clicking Shop Now"
    assert 200 <= status < 400, f"Unexpected status code: {status}"
    assert not (400 <= status < 500), f"Client error: status {status}"

    # Check URL
    expected_url = f"{base_url}products.html"
    current_url = home.get_current_url()
    assert current_url == expected_url, f"Redirected to {current_url}, expected {expected_url}"