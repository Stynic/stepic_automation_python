from selenium.webdriver.common.by import By
from selenium import webdriver
import time

try:
    line = 'http://suninjuly.github.io/wait1.html'
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(line)

    button_verify = browser.find_element(By.ID, 'verify').click()
    message = browser.find_element(By.ID, 'verify_message').text

    assert message == 'Verification was successful!', 'Хоп-хоп,ошибочка'


finally:
    time.sleep(5)
    browser.quit()