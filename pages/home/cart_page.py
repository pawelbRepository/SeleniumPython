from base.selenium_driver_helper import SeleniumDriverHelper
import utilities.custom_logger as cl
import logging
from locators.locators import CartPageLocators
from pages.home.home_page import NavigationPage
from pages.home.order_page import OrderPage


class CartPage(SeleniumDriverHelper):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.nav = NavigationPage(driver)

    def verify_summary_cart_title(self, title_eng, title_pl):
        result = self.verify_page_title(title_eng)
        if not result:
            result = self.verify_page_title(title_pl)
        return result

    def verify_number_of_product_cart(self, items=''):
        result = self.nav.get_cart_number_of_items() == items
        return result

    def click_proceed_to_checkout_button(self):
        self.element_click(*CartPageLocators.PROCEED_TO_ORDER_BUTTON)
        return OrderPage(self.driver)




