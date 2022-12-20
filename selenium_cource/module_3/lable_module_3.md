# Модуль 3

## Git
+ [Игра про GIT](https://learngitbranching.js.org/?locale=ru_RU )
+ [PyCharm+Git youtube ru](https://www.youtube.com/watch?v=9VKKZNqzPcE)
+ [книга по GIT](https://git-scm.com/book/ru/v2/)
+ [еще один мануал](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/ru/index.html)
+ [статья на хабре](https://habr.com/ru/company/intel/blog/344962/)
+ [тоже норм (step by step)](https://githowto.com/ru)


С августа 2021 гитхаб отказался от идеи доступа на сервер по АПИ через пароль. Процесс усложнился в пользу безопасности. Теперь в настройках профиля необходимо сгенерировать временный токен для доступа именно к тому функционалу который необходим.

Делается это тут Settings  => Developer Settings => Personal Access Token => Generate New Token (в настройках по выбору прав доступа поставить галку достаточно только в самом верхнем блоке касающемся доступа к репозиторию)

Копируем получившийся токен и используем его вместо пароля
использую PyCharm

## Концепция тестирования

[Пирамида тестирования](https://habr.com/ru/post/358950/)

Любой тест должен содержать:

    1. Входные данные.
    2. Тестовый сценарий, то есть набор шагов, которые надо выполнить для получения результата.
    3. Проверка ожидаемого результата.

Сообщение при проверке
    
    assert abs(-41) == 42, f'Should be absolute value of a number {abs(-41)} not equal 42'

**Конструкция** [if __name__ == "__main__"](https://www.youtube.com/watch?v=cW_-zGG4ef4)

Авто тесты на Python:
+ [unittest](https://docs.python.org/3/library/unittest.html) - встроенный
+ PyTest [статья на хабре](https://habr.com/ru/post/269759/)
+ nose

Сохраняем набор пакетов

    pip freeze > requirements.txt

Дла нового окружения, после активации запускаемЖ
    
    pip install -r requirements.txt

PyTest, для детального отчёта запускается с параметром **-v**

[Другие параметры запуска](https://gist.github.com/amatellanes/12136508b816469678c2)

Ожидаемая ошибка:
    
    import pytest
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    
    
    def test_exception1():
        try:
            browser = webdriver.Chrome()
            browser.get("http://selenium1py.pythonanywhere.com/")
            with pytest.raises(NoSuchElementException):
                browser.find_element(By.CSS_SELECTOR, "button.btn")
                pytest.fail("Не должно быть кнопки Отправить")
        finally: 
            browser.quit()
    
    def test_exception2():
        try:
            browser = webdriver.Chrome()
            browser.get("http://selenium1py.pythonanywhere.com/")
            with pytest.raises(NoSuchElementException):
                browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
                pytest.fail("Не должно быть кнопки Отправить")
        finally: 
            browser.quit()


## Фикстуры

Классический способ работы с фикстурами — создание setup- и teardown-методов в файле с тестами

[классическое примерение фикстур](https://docs.pytest.org/en/latest/how-to/xunit_setup.html)

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    link = "http://selenium1py.pythonanywhere.com/"
    
    
    class TestMainPage1():
    
        @classmethod
        def setup_class(self):
            print("\nstart browser for test suite..")
            self.browser = webdriver.Chrome()
    
        @classmethod
        def teardown_class(self):
            print("quit browser for test suite..")
            self.browser.quit()
    
        def test_guest_should_see_login_link(self):
            self.browser.get(link)
            self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    
        def test_guest_should_see_basket_link_on_the_main_page(self):
            self.browser.get(link)
            self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
    
    
    class TestMainPage2():
    
        def setup_method(self):
            print("start browser for test..")
            self.browser = webdriver.Chrome()
    
        def teardown_method(self):
            print("quit browser for test..")
            self.browser.quit()
    
        def test_guest_should_see_login_link(self):
            self.browser.get(link)
            self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    
        def test_guest_should_see_basket_link_on_the_main_page(self):
            self.browser.get(link)
            self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


**Фикстуры это декораторы**
    
    @pytest.fixture

+ [О декораторах](https://pythonworld.ru/osnovy/dekoratory.html)
+ **[Объяснение yield](https://www.youtube.com/watch?v=ZjaVrzOkpZk)**
+ [Статья на хабре](https://habr.com/ru/company/yandex/blog/242795/)
+ [Офф документация](https://docs.pytest.org/en/stable/explanation/fixtures.html)

**Примеры:**
+ test_fixture2.py
+ test_fixture3.py
+ test_fixture5.py
+ test_fixture_autouse.py


**Маркировка**

    @pytest.mark.mark_name


**Примеры:**
+
