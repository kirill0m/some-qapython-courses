from ui.pages.base_page import BasePage
from ui.pages.segments_page import SegmentsPage
from ui.pages.campaign_page import CampaignPage
from ui.locators.basic_locators import MainPageLocators
 
 
class MainPage(BasePage):
    url = 'https://target.my.com/dashboard'

    locators = MainPageLocators

    def __init__(self, driver):
        self.driver = driver

    def go_to_campaigns(self):
        self.click(MainPageLocators.nav_sample('campaigns'))
        return CampaignPage(self.driver)

    def go_to_segments(self):
        self.click(MainPageLocators.nav_sample('segments'))
        return SegmentsPage(self.driver)
    
    def login(self, data, timeout=None):
        self.click(self.locators.QUERY_LOCATOR_LOGIN)
        self.fill_out(self.locators.QUERY_LOCATOR_EMAIL, data['email'])
        self.fill_out(self.locators.QUERY_LOCATOR_PASS, data['password'])
        self.click(self.locators.GO_BUTTON_AUTH)
        return MainPage(self.driver)