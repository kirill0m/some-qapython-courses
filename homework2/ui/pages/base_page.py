from ui.locators import basic_locators
from ui.fixtures import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage(object):
    locators = basic_locators.BasePageLocators
    
    def __init__(self, driver):
        self.driver = driver
    
    def wait(self, timeout=None):
        if timeout is None:
            timeout = 20
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def fill_out(self, locator, data, timeout=None):
        field = self.find(locator, timeout=timeout)
        field.clear()
        field.send_keys(data)
