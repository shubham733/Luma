from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def load(self):
        self.page.goto(self.url)
