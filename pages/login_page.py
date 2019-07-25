from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Url have not a 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email), "Email input is not presented"
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIRST).send_keys(password), "Password first input is not presented"
        self.browser.find_element(*LoginPageLocators.PASSWORD_SECOND).send_keys(password), "Password second input is not presented"

        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click(), "Registration button is not presented"
