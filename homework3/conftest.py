import pytest
from client import ApiClient


@pytest.fixture(scope='session')
def auth_data():
    email = 'kirillomirea@gmail.com'
    password = 'cUKepf2UMeFLQvW'
    return email, password


@pytest.fixture(scope='session')
def api_client(auth_data):
    api_client = ApiClient('https://target.my.com/', *auth_data)
    return api_client
