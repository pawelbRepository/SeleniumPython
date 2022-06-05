from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
from utilities.util import Util


class SeleniumDriverHelper:
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.util = Util()

    def get_title(self):
        return self.driver.title

    def get_element(self, locator_type='', locator=''):
        element = None
        try:
            element = self.driver.find_element(locator_type, locator)
            self.log.info("Element found with locator: " + locator + " and  locator_type: " + locator_type)
        except NoSuchElementException as err:
            self.log.info("Element not found with locator: " + locator + " and  locator_type: " + locator_type + "err"
                          + str(err))
        return element

    def get_element_list(self, locator_type='', locator=''):
        """
        Get list of elements
        """
        element = None
        try:
            element = self.driver.find_elements(locator_type, locator)
            self.log.info("Element list found with locator: " + locator + " and locator_type: " + locator_type)
        except:
            self.log.info("Element list not found with locator: " + locator + " and locator_type: " + locator_type)
        return element

    def element_click(self, *locator, element=None):
        """
        Click on an element
        Either provide element or locator
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(*locator)
            element.click()
            if locator:
                self.log.info("Clicked on element with [locator] >>> '" + locator[1]
                              + "' and [locatorType] >>> '" + locator[0] + "'")
            else:
                self.log.info("Clicked on element: ")
        except StaleElementReferenceException as err:
            if locator:
                self.log.info("Cannot click on the element with [locator] >>> '" + locator[1]
                              + "' and [locatorType] >>> '" + locator[0] + "'" + "\nErrorInfo: " + str(err))
            else:
                self.log.info("Cannot click on the element: ")

    def send_keys(self, data, locator_type='', locator='', element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator_type, locator)
            self.clear_field(element=element)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locator_type: " + locator_type)
            print_stack()

    def clear_field(self, locator_type='', locator='', element=None):
        """
        Clear an element field
        """
        if element is None:
            element = self.get_element(locator_type, locator)
        element.clear()
        self.log.info("Clear field with locator: " + locator + " locator_type: " + locator_type)

    def get_element_text(self, *locator, element=None, info=''):
        """
        Get 'Text' on an element
        Either provide element or locator
        """
        text = None
        try:
            if locator: # This means if locator is not empty
                element = self.get_element(*locator)
            if element is not None:
                text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element >>> " + info)
                self.log.info("The text is >>> '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            text = None
        return text

    def is_element_displayed(self, locator_type='', locator='', element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locator_type
        """
        is_displayed = False
        # element = None
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator_type, locator)

            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed")
            else:
                self.log.info("Element not displayed")
            return is_displayed
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locator_type='', locator=''):
        """
        Check if element is present
        """
        try:
            elementList = self.driver.find_elements(locator_type, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator + " locator_type: " + str(locator_type))
                return True
            else:
                self.log.info("Element not present with locator: " + locator + " locator_type: " + str(locator_type))
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait_for_element(self, locator_type='', locator='',
                         timeout=5, poll_requency=0.5):
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=poll_requency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def verify_page_title(self, title_to_verify):
        """
        Verify the page Title

        Parameters:
            title_to_verify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.get_title()
            return self.util.verify_text_contains(actualTitle, title_to_verify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False


