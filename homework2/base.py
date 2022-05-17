import pytest
from faker import Faker
from _pytest.fixtures import FixtureRequest
from ui.pages.segments_page import SegmentsPage
from ui.pages.campaign_page import CampaignPage
from ui.pages.main_page import MainPage
from ui.pages.login_page import LoginPage


class BaseTestClass:
    driver = None
    authorize = True

    fake = Faker('ru_RU')

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            
            self.driver.refresh()
            self.main_page = MainPage(driver)

        self.campaign_page:CampaignPage = (request.getfixturevalue('campaign_page'))
        self.segments_page:SegmentsPage = (request.getfixturevalue('segments_page'))

    def generate_phone_num(self):
        return self.fake.phone_number()

    def generate_fio(self):
        return self.fake.name()

    def generate_url(self):
        return self.fake.url()

    def generate_name(self):
        return self.fake.lexify(20*'?')