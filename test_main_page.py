from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage

import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)                          # initializing the Page Object, passing the driver instance and url to the constructor
        page.open()                                             # page opening
        page.go_to_login_page()                                 # executing the page method - go to the login page
        login_page = LoginPage(browser, browser.current_url)    # initializing the Page Object, passing the driver instance and url to the constructor
        login_page.should_be_login_page()                       # executing the page method - check, if it's the login page


    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)                          # initializing the Page Object, passing the driver instance and url to the constructor
    page.open()                                             # page opening
    page.go_to_basket_page()                                # go to the basket page
    cart_page = CartPage(browser, browser.current_url)      # initializing the Page Object, passing the driver instance and url to the constructor
    cart_page.should_be_empty_cart()                        # check, if the basket is empty
    cart_page.should_be_empty_cart_text()                   # check, there is empty basket text
