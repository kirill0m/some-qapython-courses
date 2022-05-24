import pytest
import operator
from collections import Counter
from client.client import MysqlClient
from builder.builder import MysqlBuilder
from models.models import MostCommonMethodsModel
from models.models import MostCommonRequestsModel
from models.models import MostCommonUsersServerErrorModel
from models.models import BiggestRequestsClientError


class Base:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MysqlClient = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(self.mysql)

    def insert_mc_methods(self, items, top):
        methods_count = Counter(item['request'].split(' ')[0] for item in items)
        methods_count_top = methods_count.most_common(top)
        for i in methods_count_top:
            if len(i[0]) < 10:
                self.builder.create_mc_method(i[0], i[-1])

    def select_mc_methods(self):
        res = self.mysql.session.query(MostCommonMethodsModel)
        return res.all()

    def insert_mc_requests(self, items, top):
        reqs_count = Counter(item['request'].split(' ')[1] for item in items)
        reqs_count_top = reqs_count.most_common(top)
        for i in reqs_count_top:
            self.builder.create_mc_req(i[0], i[-1])

    def select_mc_requests(self):
        res = self.mysql.session.query(MostCommonRequestsModel)
        return res.all()

    def insert_mc_users_srverror(self, items, top):
        users_srverror_count = Counter(item['host'] for item in items if item['status'].startswith('5'))
        users_srverror_count_top = users_srverror_count.most_common(5)
        for i in users_srverror_count_top:
            self.builder.create_mc_user_srverror(i[0], i[-1])

    def select_mc_users_srverror(self):
        res = self.mysql.session.query(MostCommonUsersServerErrorModel)
        return res.all()

    def insert_bgst_reqs_clienterror(self, items, top):
        uniq_reqs_clerr = sorted([item for item in items if item['status'].startswith('4')], key=operator.itemgetter('request'))
        bgst_reqs_clerr_top = sorted(uniq_reqs_clerr, key=lambda item: int(item['size']) if item['size'].isdigit() else 0, reverse=True)[:top]
        for i in bgst_reqs_clerr_top:
            self.builder.create_bgst_req_clienterror(user=i['host'],
                                                     request=i['request'].split()[1],
                                                     status=i['status'],
                                                     size=i['size'])

    def select_bgst_reqs_clienterror(self):
        res = self.mysql.session.query(BiggestRequestsClientError)
        return res.all()
