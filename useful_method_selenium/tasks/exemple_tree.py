from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def calc(num1: int, num2: int):
    result = int(num1) + int(num2)
    return str(result)


try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    result = calc(num1, num2)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(result)

    button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    result_answer = browser.find_element_by_tag_name('h1').text
    print(result_answer)

finally:
    time.sleep(5)
    browser.quit()