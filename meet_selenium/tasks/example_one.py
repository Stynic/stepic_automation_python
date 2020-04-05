from selenium.webdriver.common.by import By
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/simple_form_find_task.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)


    input_first_name = browser.find_element(By.CSS_SELECTOR, '[name=first_name]').send_keys('Daniil')
    input_last_name = browser.find_element(By.NAME, 'last_name').send_keys('Kraev')
    input_city = browser.find_element(By.CLASS_NAME, 'city').send_keys('Nizhiy Novgorod')
    input_country = browser.find_element(By.ID, 'country').send_keys('Russia')
    submit_button = browser.find_element(By.ID, 'submit_button').click()


finally:
    time.sleep(30)
    browser.quit()