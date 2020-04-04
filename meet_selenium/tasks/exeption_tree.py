from selenium.webdriver.common.by import By
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    list_fill_form = browser.find_elements(By.CSS_SELECTOR, '[type="text"]')
    for element in list_fill_form:
        element.send_keys('Мой ответ')

    button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(30)
    browser.quit()