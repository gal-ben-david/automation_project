from pages.search_page import SearchPage

class TestSearch:
    def test_zara_search_returns_results(self, page):
        page_search = SearchPage(page)
        page_search.search_in_section("Woman", "jeans")
        page_search.assert_results_exist()
        
             