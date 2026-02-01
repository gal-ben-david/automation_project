import re
from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def remove_buttons(self):
        return self.page.locator("[data-qa-action*='remove']")

    def remove_first_item(self) -> None:
        expect(self.remove_buttons.first).to_be_visible(timeout=15000)
        self.remove_buttons.first.click()

        self.page.wait_for_load_state("domcontentloaded")

    def assert_empty(self) -> None:
        self.page.wait_for_timeout(1500)
        assert self.remove_buttons.count() == 0, f"Expected empty cart, but found remove buttons and header count={count}"