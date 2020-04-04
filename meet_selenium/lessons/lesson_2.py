from selenium.webdriver.common.by import By
from selenium import webdriver
import time

line = 'http://suninjuly.github.io/registration2.html'

try:
    browser = webdriver.Chrome()
    browser.get(line)

    first_name_fill = browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Daniil')
    last_name_fill = browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Kraev')
    email_fill = browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys("automation@qa.ru")

    button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    time.sleep(1)

    welcome_text = browser.find_element_by_tag_name('h1').text
    assert welcome_text == 'Congratulations! You have successfully registered!'


finally:
    time.sleep(3)
    browser.quit()