from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_product_to_cart_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_BUTTON), "Add product to cart button is not presented"

    def add_product_to_cart(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_current_product_in_cart(self):
        expected_product_name = self.browser.find_element(*ProductPageLocators.EXPECTED_PRODUCT_NAME).text
        real_product_name = self.browser.find_element(*ProductPageLocators.REAL_PRODUCT_NAME).text
        assert expected_product_name == real_product_name, "Expected {}, added {} product".format(expected_product_name,
                                                                                          real_product_name)

    def should_be_current_price(self):
        expected_price = self.browser.find_element(*ProductPageLocators.EXPECTED_PRICE).text
        real_price = self.browser.find_element(*ProductPageLocators.REAL_PRICE).text
        assert expected_price == real_price, "Expected {}, real {} price".format(expected_price, real_price)
