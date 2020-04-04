from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    select.select_by_value('1')

finally:
    time.sleep(5)
    browser.quit()