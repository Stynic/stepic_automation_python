import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class TestExampleUnittest(unittest.TestCase):
    def test_registration_one(self):

        line = 'http://suninjuly.github.io/registration1.html'

        browser = webdriver.Chrome()
        browser.get(line)
        first_name_fill = browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Daniil')
        last_name_fill = browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Kraev')
        email_fill = browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys("automation@qa.ru")
        button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        time.sleep(1)
        welcome_text = browser.find_element_by_tag_name('h1').text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!')
        time.sleep(3)
        browser.quit()

    def test_registration_two(self):

        line = 'http://suninjuly.github.io/registration2.html'

        browser = webdriver.Chrome()
        browser.get(line)
        first_name_fill = browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Daniil')
        last_name_fill = browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Kraev')
        email_fill = browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys("automation@qa.ru")
        button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        time.sleep(1)
        welcome_text = browser.find_element_by_tag_name('h1').text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!')

        time.sleep(3)
        browser.quit()


if __name__ == '__main__':
    unittest.main()