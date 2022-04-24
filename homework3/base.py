import pytest
from dataclasses import dataclass
from faker import Faker
import random


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
            relations = {'object_type': random.choice(['remarketing_player', 'remarketing_payer']),
                         'param_type': random.choice(['positive', 'negative']),
                         'param_left': random.randint(175, 365),
                         'param_right': random.randint(0, 174)
                         }
        if name is None:
            name = fake.lexify(text='??????? ??????? ???????')

        return Segment(name=name, pass_condition=pass_condition, relations=relations, logicType=logicType)


class ApiBase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        self.builder = Builder
