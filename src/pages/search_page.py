import re
from playwright.sync_api import Page, expect

class SearchPage:
    def __init__(self, page: Page):
        self.page = page

    def open_search_page(self) -> None:
        search_link = self.page.locator(
            "a[data-qa-id='header-search-text-link']"
        )

        expect(search_link).to_be_visible(timeout=10000)
        search_link.click()

    def select_section(self, section_name: str) -> None:
        btn = self.page.get_by_role("button", name=section_name, exact=True)
        expect(btn).to_be_visible(timeout=10000)
        btn.click()

        selected = self.page.locator(
            "button[data-qa-action='search-section-change'][aria-current='true']"
        )
        expect(selected).to_have_text(section_name, timeout=10000)

    def search_in_section(self,section_name: str, query: str) -> None:
        self.open_search_page()
        self.select_section(section_name)

        search_input = self.page.locator("#search-home-form-combo-input")
        expect(search_input).to_be_visible(timeout=10000)

        search_input.fill(query)
        search_input.press("Enter")

        self.wait_for_results()

    def wait_for_results(self) -> None:
        results = self.page.locator(".product-link")
        expect(results.first).to_be_visible(timeout=15000)

    def assert_results_exist(self) -> None:
        results = self.page.locator(".product-link")
        expect(results.first).to_be_visible(timeout=15000)
        assert results.count() > 0

    def open_first_product_from_results(self) -> None:
        first_product = self.page.locator("a[data-qa-action='product-click']").first

        if first_product.count() == 0:
            first_product = self.page.locator(".product-link").first

        expect(first_product).to_be_visible(timeout=15000)
        first_product.click()

        # expect(self.page).not_to_have_url(re.compile(r".*/search.*"), timeout=15000)
        expect(self.page).to_have_url(re.compile(r".*\.html.*"), timeout=15000)

