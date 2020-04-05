import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

line = 'http://selenium1py.pythonanywhere.com/'



def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get(line)
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, 'button.btn')
            pytest.fail('Не должно быть кнопки обернуто')
    finally:
        browser.quit()


def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get(line)
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, 'no_such_button.btn')
            pytest.fail('Не должно быть кнопки Отправить')
    finally:
        browser.quit()