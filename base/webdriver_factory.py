"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.get_web_driver_instance()
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class WebDriverFactory:

    def __init__(self, browser, headless):
        self.browser = browser
        self.headless = headless

    def get_web_driver_instance(self):
        base_url = 'http://sklepdemo.polomski.ayz.pl/ecommerce/index.php'
        if self.browser == 'chrome':
            service = Service('..\\..\\configfiles\\chromedriver.exe')
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            if str(self.headless) == "1":
                options.add_argument("--headless")
            driver = webdriver.Chrome(service=service, options=options)
        elif self.browser == 'firefox':
            service = Service('..\\..\\configfiles\\geckodriver.exe')
            options = FirefoxOptions()
            if str(self.headless) == "1":
                options.add_argument("--headless")
            driver = webdriver.Firefox(service=service, options=options)
        elif self.browser == 'ie':
            service = Service('..\\..\\configfiles\\IEDriverServer.exe')
            driver = webdriver.Ie(service=service)
        else:
            service = Service('..\\..\\configfiles\\chromedriver.exe')
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            if str(self.headless) == "1":
                options.add_argument("--headless")
            driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(1)
        driver.maximize_window()
        driver.get(base_url)
        return driver
