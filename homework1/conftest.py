import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption('--url', default = 'https://target.my.com/')

@pytest.fixture()
def config(request):
    url = request.config.getoption('--url')
    return {'url': url}

@pytest.fixture()
def driver(config):
    s=Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(config['url'])
    yield driver
    driver.quit()