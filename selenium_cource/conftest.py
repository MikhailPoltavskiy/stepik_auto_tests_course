import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(executable_path="C:/chromedriver/chromedriver.exe")
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
