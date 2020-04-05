from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    line = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(line)

    assert_atribute = browser.find_element(By.ID, 'price').get_attribute('style')
    print(assert_atribute)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
        )

    x = 5
    if price is True:
        browser.find_element(By.ID, 'book').click()

    input_value = browser.find_element(By.ID, 'input_value').text
    result_calc = calc(input_value)

    answer = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(result_calc)

    button_solve = browser.find_element(By.CSS_SELECTOR, '#solve').click()

    print(browser.switch_to.alert.text)


finally:
    time.sleep(5)
    browser.quit()