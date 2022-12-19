from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # вводим имя
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]').send_keys('Ivan')

    # вводим фамилию
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]').send_keys('Petrov')

    # вводим e-mail
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]').send_keys('x@x.com')

    # отправляем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)

    # жмякаем кнопку 'Submit'
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(7)
    browser.quit()
