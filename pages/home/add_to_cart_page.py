import random
from base.selenium_driver_helper import SeleniumDriverHelper
import utilities.custom_logger as cl
import logging
from pages.home.cart_page import CartPage
from pages.home.home_page import NavigationPage
from locators.locators import AddToCartPageLocators


class AddToCartPage(SeleniumDriverHelper):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.nav = NavigationPage(driver)


    def get_product_list(self):
        products_list = self.get_element_list(*AddToCartPageLocators.PRODUCT_LIST)
        return products_list

    def select_random_product(self):
        element = self.get_product_list()
        number_of_products = len(element)
        index = random.randint(0,number_of_products-1)
        self.log.info('Category: ' + self.get_title() + ' | Number of product: ' +
                      str(number_of_products) + ' | selected item: ' + str(index))
        self.element_click(element=element[index])

    def product_customization_text(self, customization_message):
        result = self.element_presence_check(*AddToCartPageLocators.PRODUCT_CUSTOMIZATION_ELEMENT)
        if result:
            self.send_keys(customization_message, *AddToCartPageLocators.PRODUCT_CUSTOMIZATION_TEXT_FIELD)
            self.element_click(*AddToCartPageLocators.PRODUCT_CUSTOMIZATION_SAVE_BUTTON)

    def click_add_to_cart(self, customization_message):
        self.product_customization_text(customization_message)
        self.element_click(*AddToCartPageLocators.ADD_TO_CART_BUTTON)

    def click_continue_shopping(self):
        self.wait_for_element(*AddToCartPageLocators.CONTINUE_SHOPPING_BUTTON, timeout=3)
        self.element_click(*AddToCartPageLocators.CONTINUE_SHOPPING_BUTTON)

    def click_proceed_to_checkout(self):
        self.element_click(*AddToCartPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        return CartPage(self.driver)

    def verify_category_title(self, title):
        result = self.verify_page_title(title)
        return result

    def add_to_cart_random_product(self, customization_message):
        self.select_random_product()
        self.click_add_to_cart(customization_message)
        self.click_continue_shopping()







