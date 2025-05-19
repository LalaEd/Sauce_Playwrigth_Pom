import pytest

@pytest.fixture()
def setup_tear_down(page) -> None:
    page.set_viewport_size({"width": 1920, "height": 606})
    page.goto("https://www.saucedemo.com/")
    yield page

