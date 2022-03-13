from turtle import right
import pytest
import time
import locators.basic_locators as bl
import names
from base import BaseTestClass


auth_data = {
    'email' : 'kirillomirea@gmail.com',
    'password' : 'cUKepf2UMeFLQvW'
}


class TestHomeWork(BaseTestClass):
    @pytest.mark.UI
    def test_login(self):
        self.login(auth_data)
        assert 'data-ga-auth-username' in self.driver.page_source


    @pytest.mark.UI
    def test_logout(self):
        self.login(auth_data)
        right_menu = self.find(bl.QUERY_LOCATOR_RIGHT_MENU)
        self.driver.execute_script('arguments[0].click()', right_menu)
        self.click(bl.GO_BUTTON_LOGOUT)
        try:
            self.find(bl.QUERY_LOCATOR_LOGIN)
            login_button_found = True
        except:
            login_button_found = False
        assert login_button_found


    @pytest.mark.UI
    def test_edit_contactinf(self):

        self.login(auth_data)
        self.click(bl.NAVIGATION['profile'])

        test_fio = names.get_full_name()
        test_num = self.generate_phone_num()

        self.fill_out(bl.QUERY_LOCATOR_FIO, test_fio)
        self.fill_out(bl.QUERY_LOCATOR_PHONE_NUM, test_num)
        self.click(bl.GO_BUTTON_SAVE)

        self.driver.refresh()

        assert self.find(
            bl.QUERY_LOCATOR_FIO
            ).get_attribute(
                'value'
                ) == test_fio and self.find(
                    bl.QUERY_LOCATOR_PHONE_NUM
                    ).get_attribute(
                        'value'
                        ) == test_num


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
        self.click(bl.NAVIGATION[query])
        assert f'/{query}' in self.driver.current_url