import pytest
from base import BaseTestClass
from selenium.common.exceptions import TimeoutException

class TestsNegativeAuthorization(BaseTestClass):
    authorize = False

    @pytest.mark.UI
    def test_empty_data(self):
        login_page = self.login_page
        login_page.login({'email': '', 'password': ''})
        assert login_page.find(login_page.locators.GO_BUTTON_AUTH_DISABLED, timeout=5)

    @pytest.mark.UI
    def test_not_valid_login(self):
        login_page = self.login_page
        login_page.login({'email': '///////////', 'password': 'ASasjkdhsa'})
        assert login_page.find(login_page.locators.LOCATOR_LOGIN_ERROR, timeout=5)

class TestsCampaign(BaseTestClass):
    @pytest.mark.UI
    def test_campaign_creation(self, file_path):
        campaign_page = self.main_page.go_to_campaigns()
        campaign_page.click_on_create_campaign_button()
        campaign_page.click_on_campaign_type('traffic')

        campaign_url = self.generate_url()

        campaign_page.send_text_to_campaign_url_field(campaign_url)
        campaign_page.click_on_advt_type('banner')
        campaign_page.upload_banner_and_sumbit_creation(file_path)
        campaign_page.confirm_campaign_creation()

        assert campaign_page.check_success_notify()


class TestsSegments(BaseTestClass):
    @pytest.mark.UI
    def test_segment_creation(self):
        segments_page = self.main_page.go_to_segments()
        unique_name = self.generate_name()
        segments_page.create_segment(unique_name)
        assert segments_page.check_if_segment_is_created(unique_name)

    @pytest.mark.UI
    def test_segment_removal(self):
        segments_page = self.main_page.go_to_segments()
        unique_name = self.generate_name()
        segments_page.create_segment(unique_name)
        if segments_page.check_if_segment_is_created(unique_name):
            segments_page.delete_segment_by_name(unique_name)
            with pytest.raises(TimeoutException):
                segments_page.find(segments_page.locators.name_cell_segment(unique_name), timeout=5)
        else:
            pytest.fail('Ошибка при создании сегмента')
