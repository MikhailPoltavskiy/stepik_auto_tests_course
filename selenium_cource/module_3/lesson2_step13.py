import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

url_1 = "http://suninjuly.github.io/registration1.html"
url_2 = "http://suninjuly.github.io/registration2.html"


class CheckRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def registration(self, url):
        browser = self.driver
        browser.implicitly_wait(5)
        browser.get(url)

        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('Ivan')
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('Petrov')
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('b@b.com')
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        browser.quit()
        return welcome_text

    def test_1(self):
        self.assertEqual(self.registration(url_1), "Congratulations! You have successfully registered!",
                         'registration failed')

    def test_2(self):
        self.assertEqual(self.registration(url_2), "Congratulations! You have successfully registered!",
                         'registration failed')


if __name__ == '__main__':
    unittest.main()
