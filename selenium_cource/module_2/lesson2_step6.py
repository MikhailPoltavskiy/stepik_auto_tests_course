from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим значения x на странице
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

    #скролим страницу
    browser.execute_script("window.scrollBy(0, 100);")

    # Вводим значение
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))

    # отмечаем checkbox 'I`m the robot'
    browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()

    # отмечаем radiobutton 'Robots rule'
    browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()

    # жмякаем кнопку 'Submit'
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(5)
    browser.quit()
