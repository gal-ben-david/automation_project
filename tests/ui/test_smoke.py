def test_homepage_loads(page):
    assert "zara" in page.url.lower()