from .pages.login_page import LoginPage


def test_guest_should_see_login_and_registration_forms(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)    # initializing the Page Object, passing the driver instance and url to the constructor
    page.open()                        # page opening
    page.should_be_login_page()        # checking the login page for registration and authorization forms, and the presence of the login substring in the url