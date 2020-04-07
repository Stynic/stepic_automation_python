import pytest

from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print('Запуск браузера')
    browser = webdriver.Chrome()
    yield browser
    print('Выключение браузера')
    browser.quit()


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")