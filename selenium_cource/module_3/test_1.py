from selenium import webdriver
from selenium.webdriver.common.by import By


def registration(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(1)
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("Homer")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("Simpson")
        email = browser.find_element(By.CSS_SELECTOR, ".third_class .third")
        email.send_keys("simpsons@mail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        return welcome_text
    except:
        browser.quit()


def test_link1():
    link = "http://suninjuly.github.io/registration1.html"
    assert registration(link) == "Congratulations! You have successfully registered!", "Error"


def test_link2():
    link = "http://suninjuly.github.io/registration2.html"
    assert registration(link) == "Congratulations! You have successfully registered!", "Error"
