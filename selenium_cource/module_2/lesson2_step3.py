from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



def calc(x, y):
    return str(int(x) + int(y))


link = "https://suninjuly.github.io/selects1.html"
# link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим значения чисел на странице
    x = browser.find_element(By.CSS_SELECTOR, '#num1').text
    y = browser.find_element(By.CSS_SELECTOR, '#num2').text

    # Выбираем из списка нужное значение
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(calc(x,y))

    # жмякаем кнопку 'Submit'
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(5)
    browser.quit()
