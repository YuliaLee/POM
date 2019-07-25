from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > [href]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators(object):
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
    PRODUCT = (By.CSS_SELECTOR, "#basket_formset .basket-items")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIRST = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_SECOND = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button.btn")


class ProductPageLocators(object):
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form>button.btn-add-to-basket")
    EXPECTED_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    REAL_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > .alert-success > .alertinner > strong")
    EXPECTED_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    REAL_PRICE = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success > .alertinner")
