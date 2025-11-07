import pytest
from pages.about_page import AboutPage

@pytest.mark.order(1)
def test_about_page_console_and_banner(page, base_url):
    about = AboutPage(page, base_url)

    # Capture console errors
    errors = about.get_console_errors()

    # Navigate to About page
    response = about.open_about_page()

    # Assert no console errors
    assert not errors, f"Console errors found: {errors}"

    # Assert status code 200–399
    status = about.get_status_code(response)
    assert status is not None, "No response returned"
    assert 200 <= status < 400, f"Unexpected status code: {status}"
    assert not (400 <= status < 500), f"Client error: status {status}"

    # Assert banner text
    title = about.get_banner_title()
    text = about.get_banner_text()
    assert title == "About FashionHub", f"Banner title mismatch: {title}"
    assert text == "Your one-stop destination for the latest fashion trends", f"Banner text mismatch: {text}"
