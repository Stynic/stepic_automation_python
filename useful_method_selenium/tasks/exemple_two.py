from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math


def cals(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    value_attribute = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    result = cals(value_attribute)

    input_text = browser.find_element(By.ID, 'answer')
    assert input_text.tag_name == 'input', 'Данный элемент не input'
    input_text.send_keys(result)

    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    answer_exemple = browser.find_element_by_tag_name('h1')
    print(str(answer_exemple))

finally:
    time.sleep(5)
    browser.quit()