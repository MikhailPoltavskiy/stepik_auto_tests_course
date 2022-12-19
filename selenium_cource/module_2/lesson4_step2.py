from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ждём, пока стоимость не будет равна 100$
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )

    # Нажимаем кнопку "book"
    browser.find_element(By.ID, 'book').click()

    # находим картинку и получаем значение атрибута valuex
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

    # вводим ответ
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))

    # жмякаем кнопку 'Submit'
    browser.find_element(By.ID, "solve").click()


finally:
    time.sleep(10)
    browser.quit()
