import pytest
import locators.basic_locators as bl
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

fake = Faker('ru_RU')

class BaseTestClass:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
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

    def login(self, data, timeout=None):
        self.click(bl.QUERY_LOCATOR_LOGIN)
        self.fill_out(bl.QUERY_LOCATOR_EMAIL, data['email'])
        self.fill_out(bl.QUERY_LOCATOR_PASS, data['password'])
        self.click(bl.GO_BUTTON_AUTH)

    def generate_phone_num(self):
        return fake.phone_number()

    def generate_fio(self):
        return fake.name()

    def content_waiter(self, locator, timeout=None):
        return self.wait(timeout).until(EC.text_to_be_present_in_element(locator))