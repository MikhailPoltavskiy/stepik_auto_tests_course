from selenium.webdriver.common.by import By
import time

link = "https://stepik.org/lesson/25969/step/8"


def test_check_login(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login")
