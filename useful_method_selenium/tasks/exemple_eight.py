from selenium.webdriver.common.by import By
from selenium import webdriver
import time

line = 'http://suninjuly.github.io/cats.html'

try:
    browser = webdriver.Chrome()
    browser.get(line)
    button = browser.find_element_by_id('button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()