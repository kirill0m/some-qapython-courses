from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.locators.basic_locators import LoginPageLocators


class LoginPage(BasePage):
    url = 'https://target.my.com/'

    locators = LoginPageLocators

    def login(self, data, timeout=None):
        self.click(self.locators.LOCATOR_LOGIN)
        self.fill_out(self.locators.LOCATOR_EMAIL, data['email'])
        self.fill_out(self.locators.LOCATOR_PASS, data['password'])
        self.click(self.locators.GO_BUTTON_AUTH)
        return MainPage(self.driver)
