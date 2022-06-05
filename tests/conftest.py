import os
from datetime import datetime
from traceback import print_stack
import pytest
from base.webdriver_factory import WebDriverFactory
import utilities.custom_logger as cl
import logging
from data import conftest
log = cl.custom_logger(logging.DEBUG)


@pytest.fixture(scope='function')
def one_time_setup(request, browser, headless):
    print('\nRunning one time setUp')

    wdf = WebDriverFactory(browser, headless)
    driver = wdf.get_web_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver
    failed_before = request.session.testsfailed
    yield driver
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        screen_shot(driver, message=test_name)
    driver.quit()
    print('\nRunning one time tearDown')


def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--headless')


# # ***************** DATA *****************
data_load = conftest.data_load


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def headless(request):
    return request.config.getoption('--headless')


def return_screenshot_file_name(message):
    dt_string = datetime.now()
    dt_string = dt_string.strftime("%d-%m-%Y_%H-%M-%S-%f")[:-3]
    file_name = str(dt_string) + "_" + message + ".png"
    return file_name

def screen_shot(driver, message):
    """
    Takes screenshot of the current open web page
    """

    file_name = return_screenshot_file_name(message)
    screenshot_directory = "../screenshots/"
    relative_file_name = screenshot_directory + file_name
    current_directory = os.path.dirname(__file__)
    destination_file = os.path.join(current_directory, relative_file_name)
    destination_directory = os.path.join(current_directory, screenshot_directory)

    try:
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
        driver.save_screenshot(destination_file)
        log.info("Screenshot save to directory: " + destination_file)
    except:
        log.error("### Exception Occurred when taking screenshot")
        print_stack()
