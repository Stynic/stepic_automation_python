from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    line = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(line)

    button = browser.find_element(By.CSS_SELECTOR, '.btn').click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    result = calc(x)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    alert_result = browser.switch_to.alert.text
    print(alert_result)

finally:
    time.sleep(4)
    browser.quit()