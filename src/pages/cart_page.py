from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page:Page):
        self.page = page

    @property
    def cart_link(self):
        return self.page.locator("a[data-qa-id='layout-header-go-to-cart']")

    @property
    def cart_count(self):
        return self.page.locator("span[data-qa-id='layout-header-go-to-cart-items-count']")

    def open(self) -> None:
        expect(self.cart_link).to_be_visible(timeout=15000)
        self.cart_link.click()
        expect(self.page).to_have_url("**/shop/cart", timeout=15000)

    def assert_count_is_at_least(self, n: int = 1, timeout_ms: int = 15000) -> None:
        expect(self.cart_count).to_be_visible(timeout=timeout_ms)
        
        count_text = self.cart_count.inner_text().strip()
        assert count_text.isdigit(), f"Cart count is not a number: '{count_text}'"
        assert int(count_text) >= n, f"Expected cart count >= {n}, got {count_text}"

    
