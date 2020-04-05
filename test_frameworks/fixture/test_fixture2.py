import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser_use():
    print("\nstart browser for test..")
    browser_use = webdriver.Chrome()
    return browser_use


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser_use):
        browser_use.get(link)
        browser_use.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser_use):
        browser_use.get(link)
        browser_use.find_element_by_css_selector(".basket-mini .btn-group > a")