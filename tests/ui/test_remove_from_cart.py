from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

class TestRemoveFromCart:
    def test_remove_item_from_shopping_bag(self, page):
        page_search = SearchPage(page)
        page_search.search_in_section("Woman", "jeans")
        page_search.open_first_product_from_results()

        product_page = ProductPage(page)
        product_page.wait_loaded()
        product_page.add_to_bag_selecting_first_in_stock_size()

        cart = CartPage(page)

        cart.remove_first_item()
        cart.assert_empty()