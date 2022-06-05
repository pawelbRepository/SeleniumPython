from base.selenium_driver_helper import SeleniumDriverHelper
import utilities.custom_logger as cl
import logging
from locators.locators import LoginPageLocators, HomePageLocators
from pages.home.home_page import HomePage
from pages.home.registration_page import RegistrationPage


class LoginPage(SeleniumDriverHelper):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_link(self):
        self.element_click(*LoginPageLocators.LOGIN_LINK)

    def click_no_account_to_register(self):
        self.element_click(*LoginPageLocators.NO_ACCOUNT_LINK)
        return RegistrationPage(self.driver)

    def enter_email(self, email):
        self.send_keys(email, *LoginPageLocators.EMIAL_FIELD)

    def enter_password(self, password):
        self.send_keys(password, *LoginPageLocators.PASSWORD_FIELD)

    def click_login_button(self):
        self.element_click(*LoginPageLocators.LOGIN_BUTTON)

    def verify_login_failed(self, expected_text_eng, expected_text_pl):
        element = self.wait_for_element(*LoginPageLocators.LOGIN_FAILED_MESSAGE, timeout=3)
        result = self.get_element_text(element=element)
        if expected_text_eng == result:
            return True
        elif expected_text_pl == result:
            return True
        return False

    def login(self, email='default@Email', password='defaultPassword'):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        return HomePage(self.driver)

    def logout(self):
        self.element_click(*HomePageLocators.LOGOUT_BUTTON)
        self.wait_for_element(*LoginPageLocators.LOGIN_LINK)
