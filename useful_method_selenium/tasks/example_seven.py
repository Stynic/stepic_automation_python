from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    line = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(line)

    magic_button = browser.find_element(By.CSS_SELECTOR, '.trollface.btn').click()
    time.sleep(1)

    new_windows = browser.window_handles[1]
    browser.switch_to.window(new_windows)
    time.sleep(1)

    value_x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    result = calc(value_x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    answer = browser.switch_to.alert.text
    print(answer)



finally:
    time.sleep(5)
    browser.quit()

