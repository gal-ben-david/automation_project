import re
from playwright.sync_api import Page, expect

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def add_button(self):
        return self.page.locator("button[data-qa-action='add-to-cart']")

    @property
    def size_list(self):
        return self.page.locator("ul.size-selector-sizes")

    @property
    def in_stock_size_buttons(self):
        return self.page.locator("ul.size-selector-sizes button[data-qa-action='size-in-stock']")

    @property
    def go_to_cart_button(self):
        return self.page.locator("button[data-qa-action='nav-to-cart']")

    def wait_loaded(self) -> None:
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.add_button).to_be_visible(timeout=15000)
    
    def add_to_bag_selecting_first_in_stock_size(self) -> None:
        expect(self.add_button).to_be_visible(timeout=15000)
        expect(self.add_button).to_be_enabled(timeout=15000)
        self.add_button.click()

        expect(self.size_list).to_be_visible(timeout=15000)

        expect(self.in_stock_size_buttons.first).to_be_visible(timeout=15000)
        self.in_stock_size_buttons.first.click()

        self.go_to_cart_from_modal()

    def go_to_cart_from_modal(self) -> None:
        expect(self.go_to_cart_button).to_be_visible(timeout=15000)
        self.go_to_cart_button.click()
        expect(self.page).to_have_url(re.compile(r".*/shop/cart.*"), timeout=15000)
