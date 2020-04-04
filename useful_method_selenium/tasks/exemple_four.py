from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    line = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(line)
    x = browser.find_element(By.ID, 'input_value').text
    result = calc(x)

    answer = browser.find_element(By.ID, 'answer').send_keys(result)
    check_box_for_robot = browser.find_element(By.ID, 'robotCheckbox').click()

    robots_rule = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', robots_rule)
    robots_rule.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


    answer = browser.find_element_by_tag_name('h1')
    print(answer)


finally:
    time.sleep(3)
    browser.quit()