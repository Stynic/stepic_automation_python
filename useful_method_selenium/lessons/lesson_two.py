from selenium.webdriver.common.by import By
from selenium import webdriver
import time

try:
    line = 'https://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(line)
    button = browser.find_element_by_tag_name("button")
    button.sc
    time.sleep(1)


    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    time.sleep(1)

    assert True

finally:
    time.sleep(5)
    browser.quit()