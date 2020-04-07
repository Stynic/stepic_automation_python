import pytest

from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    print('Запуск браузера')
    browser = webdriver.Chrome()
    yield browser
    print('Отрубаем браузер')
    browser.quit()