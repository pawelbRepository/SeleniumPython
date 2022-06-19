from pages.home.login_page import LoginPage
import utilities.custom_logger as cl
from utilities.util import Util
import logging
import unittest
import pytest


@pytest.mark.usefixtures('one_time_setup')
class TestRegistration:
    log = cl.custom_logger(logging.DEBUG)

    @pytest.mark.smoke
    @pytest.mark.test_registration
    @pytest.mark.run(order=1)
    def test_registration_with_wrong_email(self):
        self.login_page = LoginPage(self.driver)
        self.log.info('*#' * 20)
        self.log.info('test_TC-01_registration_with_wrong_email started')
        self.log.info('*#' * 20)
        self.login_page.click_login_link()
        self.registration_page = self.login_page.click_no_account_to_register()
        result1 = self.registration_page.verify_page_loaded(expected_text_eng='Create an account',
                                                            expected_text_pl='Stwórz konto')
        assert result1, 'Loading Page Failure'
        self.registration_page.set_gender()
        self.registration_page.enter_first_name("Test")
        self.registration_page.enter_last_name('Test')
        self.registration_page.enter_email(email='pawelautomatyzacja@gmail.com')
        self.registration_page.enter_password('test123')
        self.registration_page.mark_required_consents()
        self.registration_page.click_create_account_button()
        result2 = self.registration_page.verify_wrong_email_message(
            expected_text_eng='The email is already used, please choose another one or sign in',
            expected_text_pl='Ten adres e-mail jest już używany, proszę wybierz inny albo zaloguj się',)
        assert result2, 'Message Verification Failed'

    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_registration_with_valid_email(self, data_load):
        self.login_page = LoginPage(self.driver)
        self.log.info('*#' * 20)
        self.log.info('test_TC-02_registration_with_valid_email started')
        self.log.info('*#' * 20)
        self.login_page.click_login_link()
        self.registration_page = self.login_page.click_no_account_to_register()
        result1 = self.registration_page.verify_page_loaded(expected_text_eng='Create an account',
                                                            expected_text_pl='Stwórz konto')
        assert result1, 'Loading Page Failure'
        self.registration_page.set_gender()
        self.registration_page.enter_first_name("Test")
        self.registration_page.enter_last_name('Test')
        self.registration_page.enter_email(data_load[2])
        self.registration_page.enter_password('test123')
        self.registration_page.mark_required_consents()
        self.home_page = self.registration_page.click_create_account_button()
        result2 = self.home_page.verify_login_successful()
        assert result2, 'Registration Failed'


