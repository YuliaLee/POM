from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                           # открываем страницу
    page.should_be_add_product_to_cart_button()    # проверяем наличие кнопки "Добавить в корзину
    page.add_product_to_cart()            # добавляем продукт в корзину"
    page.solve_quiz_and_get_code()        # считаем результат мат. выражения и вводим ответ
    page.should_be_current_product_in_cart()     # проверяем, тот ли продукт добавился в корзину
    page.should_be_current_price()        # проверяем, соответствует ли заявленная цена цене в корзине
