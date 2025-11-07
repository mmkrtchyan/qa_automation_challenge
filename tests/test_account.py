import pytest
from pages.account_page import AccountPage

#  Console errors
@pytest.mark.order(1)
def test_account_console_errors(page, base_url):
    account = AccountPage(page, base_url)
    errors = account.get_console_errors()
    response = account.open_account()  # capture the response

    # Assert no console errors
    assert not errors, f"Console errors found: {errors}"

    # Assert status code is 200–399
    status = account.get_status_code(response)
    assert status is not None, "No response returned"
    assert 200 <= status < 400, f"Unexpected status code: {status}"
    assert not (400 <= status < 500), f"Client error: status {status}"


# Login page elements visible
@pytest.mark.order(2)
def test_account_page_elements_before_login(page, base_url):
    account = AccountPage(page, base_url)
    account.open_account()
    assert account.login_container.is_visible()
    assert account.login_header.is_visible()
    assert account.username_input.is_visible()
    assert account.password_input.is_visible()
    assert account.login_button.is_visible()
    assert account.signup_link.is_visible()


# 3️⃣ Valid login
@pytest.mark.order(3)
def test_account_valid_login(page, base_url, config):
    account = AccountPage(page, base_url)
    response = account.open_account()

    # Use username and password from config
    username = config["login"]["username"]
    password = config["login"]["password"]

    account.enter_username(username)
    account.enter_password(password)
    account.click_login()

    account.account_page_container.wait_for(state="visible")
    welcome_text = account.get_welcome_text()
    assert f"Welcome, {username}!" in welcome_text
    assert account.is_logout_visible()

    # Optional: check status code of initial navigation
    status = account.get_status_code(response)
    assert status is not None
    assert 200 <= status < 400


# 4Logout
@pytest.mark.order(4)
def test_logout(page, base_url, config):
    account = AccountPage(page, base_url)
    account.open_account()

    username = config["login"]["username"]
    password = config["login"]["password"]

    account.enter_username(username)
    account.enter_password(password)
    account.click_login()

    account.account_page_container.wait_for(state="visible")
    account.click_logout()

    assert account.login_container.is_visible()


# Registration link
@pytest.mark.order(5)
def test_registration_link(page, base_url):
    account = AccountPage(page, base_url)
    account.open_account()
    account.click_signup()

    # Wait briefly
    account.page.wait_for_timeout(1000)

    # Check URL changed from login page
    login_url = f"{base_url}account.html"
    current_url = account.get_current_url()
    assert current_url != login_url, f"BUG: Registration page did not open, still at {current_url}"


# Invalid login
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
    assert error_text is not None
    assert "Invalid username or password" in error_text
