from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)                          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                                             # открываем страницу
        page.go_to_login_page()                                 # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.should_be_login_page()                       # выполняем метод страницы - проверяем, корректна ли она

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)                          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                             # открываем страницу
    page.go_to_basket_page()                                # переходим в корзину
    cart_page = CartPage(browser, browser.current_url)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    cart_page.should_be_empty_cart()                        # проверяем, что карзина пуста
    cart_page.should_be_empty_cart_text()                   # проверяем, что есть текст о пустой корзине
