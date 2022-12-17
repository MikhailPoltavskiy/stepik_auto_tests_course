from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # нажимаем кнопку на странице
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    # Принимаем алерт
    browser.switch_to.alert.accept()

    # находим картинку и получаем значение атрибута valuex
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

    # вводим ответ
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))

    # отмечаем checkbox 'I`m the robot'
    # browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()

    # проверяем значение/атрибут по умоолчанию
    # people_radio = browser.find_element(By.ID, "peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default"

    # отмечаем radiobutton 'Robots rule'
    # browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()

    # жмякаем кнопку 'Submit'
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(10)
    browser.quit()
