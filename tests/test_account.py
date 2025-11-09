import pytest
from pages.account_page import AccountPage

# Check console errors and status code
@pytest.mark.order(1)
def test_account_console_errors(page, base_url):
    account = AccountPage(page, base_url)
    errors = account.get_console_errors()
    response = account.open_account()

    # Assert no console errors
    assert not errors, f"Console errors found: {errors}"

    # Assert status code 200–399
    status = account.get_status_code(response)
    assert status is not None, "No response returned"
    assert 200 <= status < 400, f"Unexpected status code: {status}"
    assert not (400 <= status < 500), f"Client error: status {status}"


# Check login page elements visibility
@pytest.mark.order(2)
def test_account_page_elements_before_login(page, base_url):
    account = AccountPage(page, base_url)
    account.open_account()

    assert account.login_container.is_visible(), "Login container not visible"
    assert account.login_header.is_visible(), "Login header not visible"
    assert account.username_input.is_visible(), "Username input not visible"
    assert account.password_input.is_visible(), "Password input not visible"
    assert account.login_button.is_visible(), "Login button not visible"
    assert account.signup_link.is_visible(), "Sign up link not visible"


# Successful login
@pytest.mark.order(3)
def test_account_valid_login(page, base_url, config):
    account = AccountPage(page, base_url)
    response = account.open_account()

    username = config["login"]["username"]
    password = config["login"]["password"]

    account.enter_username(username)
    account.enter_password(password)
    account.click_login()
    account.account_page_container.wait_for(state="visible")

    # Assert welcome message and logout button visible
    welcome_text = account.get_welcome_text()
    assert f"Welcome, testUser!" in welcome_text, f"Unexpected welcome text: {welcome_text}"
    assert account.is_logout_button_visible(), "Logout button not visible after login"

    # Assert status code 200–399
    status = account.get_status_code(response)
    assert status is not None, "No response returned"
    assert 200 <= status < 400, f"Unexpected status code: {status}"
    assert not (400 <= status < 500), f"Client error: status {status}"


# Logout
@pytest.mark.order(4)
def test_logout(page, base_url, config):
    account = AccountPage(page, base_url)

    # Wait until account page is visible
    account.account_page_container.wait_for(state="visible")

    # Click logout
    account.click_logout()

    # Assert returned to login page
    assert account.login_container.is_visible(), "Did not return to login page after logout"


# Open Registration page
@pytest.mark.order(5)
def test_open_registration_page(page, base_url):
    account = AccountPage(page, base_url)
    account.open_account()

    account.click_signup()
    account.page.wait_for_timeout(1000)

    # Assert URL changed from login page
    login_url = f"{base_url}account.html"
    current_url = account.get_current_url()
    assert current_url != login_url, f"BUG: Registration page did not open, still at {current_url}"


# Invalid login with wrong credentials
@pytest.mark.order(6)
def test_login_invalid(page, base_url):
    account = AccountPage(page, base_url)
    account.open_account()

    account.enter_username("wronguser")
    account.enter_password("wrongpass")
    account.click_login()

    error_locator = account.page.locator("#errorMessage")
    error_locator.wait_for(state="visible", timeout=2000)

    error_text = error_locator.text_content()
    assert error_text is not None, "Expected error message for invalid login"
    assert "Invalid username or password" in error_text, f"Unexpected error text: {error_text}"
