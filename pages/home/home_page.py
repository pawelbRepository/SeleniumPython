from selenium.webdriver import ActionChains, Keys
from base.selenium_driver_helper import SeleniumDriverHelper
import utilities.custom_logger as cl
import logging
from locators.locators import NavigationPageLocators, HomePageLocators


class HomePage(SeleniumDriverHelper):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.nav = NavigationPage(driver)

    def verify_login_successful(self):
        element = self.wait_for_element(*HomePageLocators.LOGOUT_BUTTON)
        result = self.is_element_displayed(element=element)
        return result

    def verify_title_after_login(self, title_eng, title_pl):
        result = self.verify_page_title(title_eng)
        if not result:
            result = self.verify_page_title(title_pl)
        return result


class NavigationPage(SeleniumDriverHelper):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_main_page(self):
        self.element_click(*NavigationPageLocators.MAIN_PAGE)

    def click_category_clothes(self):
        self.element_click(*NavigationPageLocators.CATEGORY_CLOTHES)

    def click_category_clothes_men(self):
        drop_down = self.get_element(*NavigationPageLocators.CATEGORY_CLOTHES)
        actions = ActionChains(self.driver)
        actions.move_to_element(drop_down)
        actions.perform()
        self.element_click(*NavigationPageLocators.CATEGORY_CLOTHES_MEN)

    def click_category_clothes_women(self):
        drop_down = self.get_element(*NavigationPageLocators.CATEGORY_CLOTHES)
        actions = ActionChains(self.driver)
        actions.move_to_element(drop_down)
        actions.perform()
        self.element_click(*NavigationPageLocators.CATEGORY_CLOTHES_WOMEN)

    def click_category_accessories(self):
        self.element_click(*NavigationPageLocators.CATEGORY_ACCESSORIES)

    def click_category_accessories_stationery(self):
        drop_down = self.get_element(*NavigationPageLocators.CATEGORY_ACCESSORIES)
        actions = ActionChains(self.driver)
        actions.move_to_element(drop_down)
        actions.perform()
        self.element_click(*NavigationPageLocators.CATEGORY_ACCESSORIES_STATIONERY)

    def click_category_accessories_home(self):
        drop_down = self.get_element(*NavigationPageLocators.CATEGORY_ACCESSORIES)
        actions = ActionChains(self.driver)
        actions.move_to_element(drop_down)
        actions.perform()
        self.element_click(*NavigationPageLocators.CATEGORY_ACCESSORIES_HOME)

    def click_category_art(self):
        self.element_click(*NavigationPageLocators.CATEGORY_ART)

    def change_language_to_polish(self):
        self.element_click(*NavigationPageLocators.LANGUAGE_DROP_DOWN)
        self.element_click(*NavigationPageLocators.LANGUAGE_OPTION_POLISH)

    def change_language_to_english(self):
        self.element_click(*NavigationPageLocators.LANGUAGE_DROP_DOWN)
        self.element_click(*NavigationPageLocators.LANGUAGE_OPTION_ENGLISH)

    def enter_search_phrase(self, phrase):
        self.send_keys(phrase, *NavigationPageLocators.SEARCH_FIELD)
        self.send_keys(Keys.ENTER, *NavigationPageLocators.SEARCH_FIELD)

    def click_logout(self):
        self.element_click(*NavigationPageLocators.LOGOUT)

    def click_account(self):
        self.element_click(*NavigationPageLocators.ACCOUNT)

    def click_cart(self):
        self.element_click(*NavigationPageLocators.CART)

    def get_cart_number_of_items(self):
        element = self.get_element(*NavigationPageLocators.CART_NUMBER_OF_ITEMS)
        number_of_items = element.text
        number_of_items = number_of_items.replace('(', '').replace(')', '')
        return number_of_items
