from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = " https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # находим капчу и вычисляем значение
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    # вводим ответ
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    # отмечаем checkbox 'I`m the robot'
    browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()

    # отмечаем radiobutton 'Robots rule'
    browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()

    # жмякаем кнопку 'Submit'
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(10)
    browser.quit()
