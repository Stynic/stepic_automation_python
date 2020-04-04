from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    result = calc(x)
    input_result = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    robot_check_box = browser.find_element(By.ID, 'robotCheckbox').click()
    robot_radio_button = browser.find_element(By.ID, 'robotsRule').click()
    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn').click()

    text_notification = browser.find_element_by_tag_name('h1').text
    print(text_notification)

finally:
    time.sleep(5)
    browser.quit()