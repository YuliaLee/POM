from .pages.login_page import LoginPage


def test_guest_should_see_login_and_registration_forms(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                        # открываем страницу
    page.should_be_login_page()        # проиводим проверки страницы логина на наличие форм регистрации, авторизации и наличия в url подстроки login