import time

from pages.about_page import AboutPage

#Check console errors and status code
def test_about_page_console_errors(page, base_url):
    about = AboutPage(page, base_url)

    # Collect console errors
    errors = about.get_console_errors()
    response = about.open_about_page()

    assert not errors, f"Console errors found: {errors}"

    # Assert status code is 200–399
    status = about.get_status_code(response)
    assert status is not None, "No response returned"
    assert 200 <= status < 400, f"Unexpected status code: {status}"
    assert not (400 <= status < 500), f"Client error: status {status}"

#Check banner title and text
def test_about_page_banner(page, base_url):
    about = AboutPage(page, base_url)
    about.open_about_page()  # Navigate to About page

    # Assert banner title
    title = about.get_header_title()
    assert title == "About FashionHub", f"Banner title mismatch: {title}"

    # Assert banner text
    text = about.get_header_text()
    assert text == "Your one-stop destination for the latest fashion trends", f"Banner text mismatch: {text}"
