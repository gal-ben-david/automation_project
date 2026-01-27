import pytest
from pages.help_page import HelpPage


class TestRegionChange:

    @pytest.mark.parametrize(
    "store_value, expected_store",
    [
        ("it", "Italy"),
        ("fr", "France"),
        ("de", "Germany"),
    ]
)

    def test_change_region(self, page, store_value, expected_store):
        help_page = HelpPage(page)

        help_page.open_home()
        help_page.open_help()

        help_page.open_change_store_modal()
        help_page.choose_store_by_value(store_value)   # Italy is value="it"
        help_page.continue_to_store()

        help_page.assert_store_changed(expected_store)
