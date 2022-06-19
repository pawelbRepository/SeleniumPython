from pages.home.add_to_cart_page import AddToCartPage
from pages.home.login_page import LoginPage
from pages.home.home_page import NavigationPage
import utilities.custom_logger as cl
import logging
import pytest


@pytest.mark.usefixtures('one_time_setup')
class TestAddToCart:
    log = cl.custom_logger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def object_setup(self, one_time_setup):
        self.add_to_cart_page = AddToCartPage(self.driver)
        self.navigation_page = NavigationPage(self.driver)

    @pytest.mark.smoke
    @pytest.mark.test_add_to_cart
    @pytest.mark.run(order=1)
    def test_add_products_to_cart(self, data_load):
        self.login_page = LoginPage(self.driver)
        self.log.info('*#' * 20)
        self.log.info('test_TC-05_add_products_to_cart started')
        self.log.info('*#' * 20)
        self.home_page = self.login_page.login(data_load[0], data_load[1])
        result_login = self.home_page.verify_login_successful()
        assert result_login, 'Login Failed'

        self.navigation_page.click_category_clothes_men()
        result_men_page = self.add_to_cart_page.verify_category_title('Men')
        assert result_men_page, 'Wrong page'
        self.add_to_cart_page.add_to_cart_random_product('customization_text')

        self.navigation_page.click_category_clothes_women()
        result_women_page = self.add_to_cart_page.verify_category_title('Women')
        assert result_women_page, 'Wrong page'
        self.add_to_cart_page.add_to_cart_random_product('customization_text')

        self.navigation_page.click_category_accessories_stationery()
        result_stationery_page = self.add_to_cart_page.verify_category_title('Stationery')
        assert result_stationery_page, 'Wrong page'
        self.add_to_cart_page.add_to_cart_random_product('customization_text')

        self.navigation_page.click_category_accessories_home()
        result_accessories_page = self.add_to_cart_page.verify_category_title('Home Accessories')
        assert result_accessories_page, 'Wrong page'
        self.add_to_cart_page.add_to_cart_random_product('customization_text')

        self.navigation_page.click_category_art()
        result_art_page = self.add_to_cart_page.verify_category_title('Art')
        assert result_art_page, 'Wrong page'
        self.add_to_cart_page.add_to_cart_random_product('customization_text')

        self.cart_page = self.add_to_cart_page.click_proceed_to_checkout()
        result_summary_page = self.cart_page.verify_summary_cart_title('Cart', 'Koszyk')
        assert result_summary_page, 'Wrong page'

        result_cart_verification = self.cart_page.verify_number_of_product_cart(items='5')
        assert result_cart_verification, 'Wrong number of items'
