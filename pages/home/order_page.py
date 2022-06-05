from base.selenium_driver_helper import SeleniumDriverHelper
import utilities.custom_logger as cl
import logging
from locators.locators import OrderPageLocators


class OrderPage(SeleniumDriverHelper):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_verification_text(self):
        result = self.get_element_text(*OrderPageLocators.ORDER_PAGE_VERIFICATION_TEXT_ELEMENT)
        return result

    def verify_page_loaded(self):
        result = self.is_element_displayed(*OrderPageLocators.ORDER_PAGE_VERIFICATION_TEXT_ELEMENT)
        return result

    def verify_order_confirmed(self):
        result = self.is_element_displayed(*OrderPageLocators.ORDER_CONFIRMATION_TEXT_ELEMENT)
        return result

    def verify_personal_information_section(self):
        result = self.is_element_displayed(*OrderPageLocators.PERSONAL_INFORMATION_ELEMENT)
        return result

    def verify_addresses_section(self):
        result = self.is_element_displayed(*OrderPageLocators.ADDRESSES_SECTION_ELEMENT)
        return result

    def verify_shipping_section(self):
        result = self.is_element_displayed(*OrderPageLocators.SHIPPING_SECTION_ELEMENT)
        return result

    def verify_payment_section(self):
        result = self.is_element_displayed(*OrderPageLocators.PAYMENT_SECTION_ELEMENT)
        return result

    def go_to_addresses_section(self):
        self.element_click(*OrderPageLocators.CONTINUE_BUTTON)

    def enter_address(self, address):
        self.send_keys(address, *OrderPageLocators.ADDRESSES_SECTION_ADDRESS_FIELD)

    def enter_post_code(self, postal_code):
        self.send_keys(postal_code, *OrderPageLocators.ADDRESSES_SECTION_POST_CODE_FIELD)

    def enter_city(self, city):
        self.send_keys(city, *OrderPageLocators.ADDRESSES_SECTION_CITY_FIELD)

    def input_required_address_data(self, address, postal_code, city):
        self.enter_address(address)
        self.enter_post_code(postal_code)
        self.enter_city(city)

    def confirm_address_data(self):
        self.element_click(*OrderPageLocators.CONFIRM_ADDRESS_BUTTON)

    def confirm_shipping_data(self):
        self.element_click(*OrderPageLocators.CONFIRM_SHIPPING_BUTTON)

    def set_payment_option(self):
        self.element_click(*OrderPageLocators.SET_PAYMENT_OPTION_RADIO_BUTTON)

    def mark_conditions_checkbox(self):
        self.element_click(*OrderPageLocators.MARK_CONDITIONS_CHECKBOX)

    def payment_confirmation(self):
        self.set_payment_option()
        self.mark_conditions_checkbox()
        self.element_click(*OrderPageLocators.CONFIRM_PAYMENT_BUTTON)
