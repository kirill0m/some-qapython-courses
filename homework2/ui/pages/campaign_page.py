from ui.pages.base_page import BasePage
from ui.locators.basic_locators import CampaignLocators
 

class CampaignPage(BasePage):
    locators = CampaignLocators

    def __init__(self, driver):
        self.driver = driver

    def click_on_campaign_type(self, type):
        self.click(self.locators.campaign_creation(type))

    def click_on_create_campaign_button(self):
        self.click(self.locators.LOCATOR_CREATE_CAMPAIGN)

    def send_text_to_campaign_url_field(self, url):
        self.fill_out(self.locators.LOCATOR_CAMPAIGN_URL, url)

    def click_on_advt_type(self, type):
        self.click(self.locators.advt_patterns(type))

    def upload_banner_and_sumbit_creation(self, file_path):
        self.find(self.locators.LOCATOR_UPLOAD_BANNER).send_keys(file_path)
        self.click(self.locators.LOCATOR_SUBMIT_BANNER_CREATION)

    def confirm_campaign_creation(self):
        self.click(self.locators.LOCATOR_SUBMIT_CAMPAIGN_CREATION)

    def check_success_notify(self):
        self.find(self.locators.LOCATOR_MAIN_TABLE)
        return True if self.find(self.locators.LOCATOR_CREATION_NOTIFY) else False
