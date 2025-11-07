class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        """Navigate to a given URL and return the response."""
        return self.page.goto(url)

    def get_console_errors(self):
        """Capture JavaScript console errors."""
        console_errors = []
        self.page.on(
            "console",
            lambda msg: console_errors.append(msg.text) if msg.type == "error" else None
        )
        return console_errors

    def get_status_code(self, response):
        """Return the response status code, without asserting."""
        if not response:
            return None
        return response.status

    def get_current_url(self):
        """Returns the current URL after navigation"""
        return self.page.url