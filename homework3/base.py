import pytest
from dataclasses import dataclass
from faker import Faker


fake = Faker()


class Builder:
    @staticmethod
    def campaign(name=None, objective='traffic', package_id=961):
        @dataclass
        class Campaign:
            name: str
            objective: str
            package_id: int

        if name is None:
            name = fake.lexify(text='??????? ??????? ???????')

        return Campaign(name=name, objective=objective, package_id=package_id)

    @staticmethod
    def segment(name=None, pass_condition=1, relations=None, logicType='or'):
        @dataclass()
        class Segment:
            name: str
            pass_condition: int
            relations: dict
            logicType: str

        if relations is None:
            relations = {'object_type': 'segment', 'object_id': 1585154}

        if name is None:
            name = fake.lexify(text='??????? ??????? ???????')

        return Segment(name=name, pass_condition=pass_condition, relations=relations, logicType=logicType)


class ApiBase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        self.builder = Builder
        api_client.post_login()
