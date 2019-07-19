from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form>button.btn-add-to-basket")
    EXPECTED_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    REAL_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > .alert-success > .alertinner > strong")
    EXPECTED_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    REAL_PRICE = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success > .alertinner")

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")