from pages.home.login_page import LoginPage
import utilities.custom_logger as cl
import logging
import unittest
import pytest


@pytest.mark.usefixtures('one_time_setup')
class TestLogin:
    log = cl.custom_logger(logging.DEBUG)

    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.login_page = LoginPage(self.driver)
        self.log.info('*#' * 20)
        self.log.info('test_TC1_invalidLogin started')
        self.log.info('*#' * 20)
        self.login_page.login('wrong@email', 'wrongPassword')
        result = self.login_page.verify_login_failed()
        assert result, 'Verification Failed'

    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    def test_valid_login(self, data_load):
        self.login_page = LoginPage(self.driver)
        self.log.info('*#' * 20)
        self.log.info('test_TC2_validLogin started')
        self.log.info('*#' * 20)
        self.home_page = self.login_page.login(data_load[0], data_load[1])
        result1 = self.home_page.verify_title_after_login('My account', 'Moje konto')
        assert result1, 'Login Failed'
        result2 = self.home_page.verify_login_successful()
        assert result2, 'Verification Failed'

