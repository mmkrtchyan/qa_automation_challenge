from pages.home_page import HomePage

def test_console_errors(page, base_url):
    home = HomePage(page)
    errors = home.get_console_errors()
    response = home.goto(base_url)  # capture response

    # Assert no console errors
    assert not errors, f"Console errors found: {errors}"

    # Assert status code is 200–399
    status = home.get_status_code(response)
    assert status is not None, "No response returned"
    assert 200 <= status < 400, f"Unexpected status code: {status}"
    assert not (400 <= status < 500), f"Client error: status {status}"

def test_home_screen(page,base_url):
    home = HomePage(page)
    response = home.goto(base_url)

    header = home.get_header_text()
    assert header == "FashionHub", f"Header text mismatch: {header}"

    title = home.get_title_text()
    assert title == "Welcome to FashionHub", f"Title text mismatch: {title}"

    status = home.get_status_code(response)

    assert status is not None, "No response returned"
    assert 200 <= status < 400, f"Unexpected status code: {status}"

def test_shop_now(page,base_url):
    home = HomePage(page)
    # Assert button visibility and clickability
    assert home.is_shop_now_visible(), "'Shop Now' button is not visible"
    assert home.is_shop_now_enabled(), "'Shop Now' button is not clickable"

    # Click button
    response = home.click_shop_now()

    # Assert redirect URL
    expected_url = "https://pocketaces2.github.io/fashionhub/products.html"
    current_url = home.get_current_url()
    assert current_url == expected_url, f"Redirected to {current_url}, expected {expected_url}"

    # Check status: must be 200 or 3xx
    status = home.get_status_code(response)
    assert status is not None, "No response returned"
    assert 200 <= status < 400, f"Unexpected status code: {status}"
    assert not (400 <= status < 500), f" Client error: status {status}"
