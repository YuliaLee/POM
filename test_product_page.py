from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                           # открываем страницу
    page.should_be_add_product_to_cart_button()    # проверяем наличие кнопки "Добавить в корзину
    page.add_product_to_cart()            # добавляем продукт в корзину"
    page.solve_quiz_and_get_code()        # считаем результат мат. выражения и вводим ответ
    page.should_be_current_product_in_cart()     # проверяем, тот ли продукт добавился в корзину
    page.should_be_current_price()        # проверяем, соответствует ли заявленная цена цене в корзине

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()                                 # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    login_page.should_be_login_page()