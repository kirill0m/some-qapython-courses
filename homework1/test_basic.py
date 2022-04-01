import pytest
import locators.basic_locators as bl
from base import BaseTestClass
from selenium.common.exceptions import ElementClickInterceptedException


auth_data = {
    'email' : 'kirillomirea@gmail.com',
    'password' : 'cUKepf2UMeFLQvW'
}


class TestHomeWork(BaseTestClass):
    @pytest.mark.UI
    def test_login(self):
        self.login(auth_data)
        assert self.find(bl.QUERY_LOCATOR_RIGHT_MENU)

    @pytest.mark.UI
    def test_logout(self):
        self.login(auth_data)
        right_menu = self.find(bl.QUERY_LOCATOR_RIGHT_MENU)
        logout_clicked = False
        while not logout_clicked:
            try:
                self.driver.execute_script('arguments[0].click()', right_menu)
                self.click(bl.GO_BUTTON_LOGOUT)
                logout_clicked = True
            except (ElementClickInterceptedException):
                pass
        assert self.find(bl.QUERY_LOCATOR_LOGIN)


    @pytest.mark.UI
    def test_edit_contactinf(self):

        self.login(auth_data)
        self.click(bl.nav_sample('profile'))

        test_fio = self.generate_fio()
        test_num = self.generate_phone_num()

        self.fill_out(bl.QUERY_LOCATOR_FIO, test_fio)
        self.fill_out(bl.QUERY_LOCATOR_PHONE_NUM, test_num)
        self.click(bl.GO_BUTTON_SAVE)

        self.driver.refresh()

        assert self.find(bl.QUERY_LOCATOR_FIO).get_attribute('value') == test_fio \
            and self.find(bl.QUERY_LOCATOR_PHONE_NUM).get_attribute('value') == test_num

    @pytest.mark.UI
    @pytest.mark.parametrize(
        'query',
        [
            pytest.param(
                'billing'
            ),
            pytest.param(
                'statistics'
            ),
        ],
    )
    def test_redirect(self, query):
        self.login(auth_data)
        self.click(bl.nav_sample(query))
        assert self.find(bl.pages_identifiers(query))