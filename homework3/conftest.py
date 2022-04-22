import pytest
from client import ApiClient


@pytest.fixture(scope='session')
def credentials():
    with open("homework3\\creds.txt", 'r') as f:
        email = f.readline().strip()
        password = f.readline().strip()
    return email, password


@pytest.fixture(scope='session')
def api_client(credentials):
    api_client = ApiClient('https://target.my.com/', *credentials)
    api_client.post_login()
    return api_client
