import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.login_page import LoginPage
from ui.pages.segments_page import SegmentsPage
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.campaign_page import CampaignPage


@pytest.fixture()
def driver(config):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(config['url'])
    yield driver
    driver.quit()

@pytest.fixture()
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture()
def main_page(driver):
    return MainPage(driver=driver)

@pytest.fixture()
def campaign_page(driver):
    return CampaignPage(driver=driver)

@pytest.fixture()
def segments_page(driver):
    return SegmentsPage(driver=driver)

@pytest.fixture
def file_path(repo_root):
    return os.path.join(repo_root, 'files', 'userdata.jpg')

@pytest.fixture(scope='session')
def auth_data():
    auth_data = {
    'email' : 'kirillomirea@gmail.com',
    'password' : 'cUKepf2UMeFLQvW'
    }
    return auth_data

@pytest.fixture(scope='session')
def cookies(auth_data, config):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(config['url'])
    login_page = LoginPage(driver)
    login_page.login(auth_data)
    cookies = driver.get_cookies()
    driver.quit()
    return cookies
