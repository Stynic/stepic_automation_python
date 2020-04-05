import math
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

link = 'http://suninjuly.github.io/find_link_text'
search_value_formula = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Выбираем элемент по тексту(По расчитанной формуле)
    text_math_pi = browser.find_element_by_link_text(search_value_formula).click()

    # Заполняем поля текстом для отправки формы
    input_first_name = browser.find_element(By.CSS_SELECTOR, '[name=first_name]').send_keys('Daniil')
    input_last_name = browser.find_element(By.NAME, 'last_name').send_keys('Kraev')
    input_city = browser.find_element(By.CLASS_NAME, 'city').send_keys('Nizhiy Novgorod')
    input_country = browser.find_element(By.ID, 'country').send_keys('Russia')
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


finally:
    time.sleep(30)
    browser.quit()