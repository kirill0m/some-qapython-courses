import pytest
from mock.flask_mock import SURNAME_DATA
from faker import Faker

fake = Faker('en_US')


class ApiBase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, client):
        self.client = client


class TestMock(ApiBase):
    @pytest.mark.put
    def test_user_update(self):
        name = fake.name()
        SURNAME_DATA[name[0]] = name[1]
        self.client.create_user(name)
        new_sname = fake.name().split()[-1]
        self.client.request('PUT',
                            location=f'/update_user/{name[0]}',
                            json={'surname': new_sname})
        resp = self.client.request('GET',
                                   location=f'/get_user/{name[0]}')
        assert resp.json()['surname'] == new_sname

    @pytest.mark.delete
    def test_surname_delete(self):
        name = fake.name()
        SURNAME_DATA[name[0]] = name[1]
        self.client.create_user(name)
        self.client.request('DELETE', location=f'/delete_surname/{name[0]}')
        resp = self.client.request('GET', location=f'/get_user/{name[0]}')
        assert resp.json()['surname'] == None
