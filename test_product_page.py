from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage

import pytest
import time


@pytest.mark.user
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)            # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                                  # открываем страницу
        page.should_be_add_product_to_cart_button()  # проверяем наличие кнопки "Добавить в корзину
        page.add_product_to_cart()                   # добавляем продукт в корзину
        page.solve_quiz_and_get_code()               # считаем результат мат. выражения и вводим ответ
        page.should_be_current_product_in_cart()     # проверяем, тот ли продукт добавился в корзину
        page.should_be_current_price()               # проверяем, соответствует ли заявленная цена цене в корзине


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_cart_button()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_current_product_in_cart()
    page.should_be_current_price()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty_cart()
    cart_page.should_be_empty_cart_text()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_can_see_added_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.go_to_basket_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_added_product_in_cart()


