from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math
import pytest


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()



list_line = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
    ]


@pytest.mark.parametrize("line", list_line)
def test_fixture_line(browser, line):
    try:
        answer = str(math.log(int(time.time())))
        browser.get(line)
        browser.implicitly_wait(5)
        fill_answer = browser.find_element(By.CSS_SELECTOR, '.textarea')
        fill_answer.send_keys(answer)
        browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
        result = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
        print(result)
    finally:
        time.sleep(2)