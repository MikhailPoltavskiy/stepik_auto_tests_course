import os
import time
import math
from dotenv import load_dotenv
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
# answer = math.log(int(time.time()))

list_link = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
             'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
             'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
             'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']


@pytest.mark.parametrize('link', list_link)
def test_logon_stepik(browser, link):
    browser.implicitly_wait(10)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '#ember33').click()
    browser.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys(os.getenv("LOGIN_STEPIK"))
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(os.getenv("PASSWORD_STEPIK"))
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, '.ember-text-area').send_keys(math.log(int(time.time())))
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission'))
    )
    browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
    time.sleep(5)
    message = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint').text
    print(f'message: {message}')
    assert message == 'Correct!'


# button.again-btn.white
# @pytest.mark.parametrize('link', list_link)
# def test_logon_stepik_unclick(browser):
#     browser.implicitly_wait(10)
#     link = 'https://stepik.org/lesson/236896/step/1'
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, '#ember33').click()
#     browser.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys(os.getenv("LOGIN_STEPIK"))
#     browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(os.getenv("PASSWORD_STEPIK"))
#     browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
#     time.sleep(5)
#     browser.find_element(By.CSS_SELECTOR, 'button.again-btn.white').click()
#     browser.switch_to.alert.accept()
    # modal - popup__container
