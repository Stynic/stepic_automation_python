from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

line = 'http://suninjuly.github.io/file_input.html'
path = os.path.abspath(os.path.dirname(__name__))
path_file = os.path.join(path, 'exemple_five_text.txt')

try:
    browser = webdriver.Chrome()
    browser.get(line)

    first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Daniil')
    last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Kraev')
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('email@mail.ru')

    file_loaded = browser.find_element(By.CSS_SELECTOR, '#file').send_keys(path_file)

    button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(1)
    answer = browser.find_element_by_tag_name('h1').text
    print(answer)



finally:
    time.sleep(5)
    browser.quit()