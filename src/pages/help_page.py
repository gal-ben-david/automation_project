import re
from playwright.sync_api import Page, expect

class HelpPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def current_store_button(self):
        return self.page.locator("button[data-qa-action='change-store-current-store']")

    @property
    def store_select(self):
        return self.page.locator("select[name='selectedStore']")

    @property
    def continue_button(self):
        return self.page.locator("button[data-qa-action='go-to-store']")

    def open_home(self) -> None:
        self.page.goto("https://www.zara.com/il/en/", wait_until="domcontentloaded")

    def open_help(self) -> None:
        help_link = self.page.locator(
            "a[data-qa-id='notify-help-center-click']"
        )

        expect(help_link).to_be_visible(timeout=10000)
        help_link.click()

    def open_change_store_modal(self) -> None:
        expect(self.current_store_button).to_be_visible(timeout=15000)
        self.current_store_button.scroll_into_view_if_needed()
        self.current_store_button.click()

        expect(self.store_select).to_be_visible(timeout=15000)

    def choose_store_by_value(self, store_value: str) -> None:
        expect(self.store_select).to_be_visible(timeout=15000)
        self.store_select.select_option(value=store_value)

    def continue_to_store(self) -> None:
        expect(self.continue_button).to_be_visible(timeout=15000)
        expect(self.continue_button).to_be_enabled(timeout=15000)
        self.continue_button.click()
        self.page.wait_for_load_state("domcontentloaded")

    def assert_store_changed(self, expected_store="Italy") -> None:
        expect(self.current_store_button).to_be_visible(timeout=15000)
        text = self.current_store_button.inner_text().strip()

        normalized = text.lower()
        expected = expected_store.lower()

        assert expected in normalized, (
        f"Expected store to contain '{expected_store}', got '{text}'"
    )