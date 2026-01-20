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

    def search(self, query: str) -> None:
        self.open_search_page()

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