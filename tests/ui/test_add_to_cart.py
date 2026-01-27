from pages.cart_page import CartPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage

class TestAddToCart:
    def test_add_first_item_to_cart(self, page):
        page_search = SearchPage(page)
        page_search.search_in_section("Woman", "jeans")
        page_search.open_first_product_from_results()

        product_page = ProductPage(page)
        product_page.wait_loaded()
        product_page.add_to_bag_selecting_first_in_stock_size()

        # cart = CartPage(page)
        # cart.assert_count_is_at_least(1)
        # cart.open()

