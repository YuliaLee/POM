from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCT), \
            "Basket is not emtpy"

    def should_be_empty_cart_text(self):
        assert "empty" in self.browser.find_element(*CartPageLocators.EMPTY_MESSAGE).text, \
            "Full cart message is presented, but should not be"

    def should_be_added_product_in_cart(self):
        assert self.is_element_present(*CartPageLocators.PRODUCT), \
             "Basket is empty"