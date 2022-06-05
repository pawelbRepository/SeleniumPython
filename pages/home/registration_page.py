from base.selenium_driver_helper import SeleniumDriverHelper
import utilities.custom_logger as cl
import logging

from pages.home.home_page import HomePage
from locators.locators import RegistrationPageLocators


class RegistrationPage(SeleniumDriverHelper):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_loaded(self, expected_text_eng, expected_text_pl):
        element = self.wait_for_element(*RegistrationPageLocators.REGISTRATION_PAGE_EXPECTED_TEXT_ELEMENT)
        result = self.get_element_text(element=element)
        if expected_text_eng == result:
            return True
        elif expected_text_pl == result:
            return True
        return False

    def set_gender(self):
        self.element_click(*RegistrationPageLocators.RADIOBUTTON_GENDER_MEN)

    def enter_first_name(self, first_name):
        self.send_keys(first_name, *RegistrationPageLocators.FIRST_NAME_FILED)

    def enter_last_name(self, last_name):
        self.send_keys(last_name, *RegistrationPageLocators.LAST_NAME_FIELD)

    def enter_email(self, email):
        self.send_keys(email, *RegistrationPageLocators.EMAIL_FIELD)

    def enter_password(self, password):
        self.send_keys(password, *RegistrationPageLocators.PASSWORD_FIELD)

    def mark_required_consents(self):
        self.element_click(*RegistrationPageLocators.CONSENT_1_OF_2)
        self.element_click(*RegistrationPageLocators.CONSENT_2_OF_2)

    def verify_wrong_email_message(self, expected_text_eng, expected_text_pl):
        element = self.wait_for_element(*RegistrationPageLocators.WRONG_EMAIL_ERROR_MESSAGE_FIELD)
        result = self.get_element_text(element=element)
        if expected_text_eng == result:
            return True
        elif expected_text_pl == result:
            return True
        return False

    def click_create_account_button(self):
        self.element_click(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)
        return HomePage(self.driver)
