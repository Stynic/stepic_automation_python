from selenium.webdriver.common.by import By
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    list_fill_form = browser.find_elements(By.CLASS_NAME, 'form-group')
    for element in list_fill_form:
        element.find_element(By.CSS_SELECTOR, 'input').send_keys('Мой ответ')

    #button_submit = browser.find_element(By.XPATH, "//*[text()='Submit']").click()
    contains_button_submit = browser.find_element(By.XPATH, "//button[contains(text(), 'Sub')]").click()

finally:
    time.sleep(30)
    browser.quit()