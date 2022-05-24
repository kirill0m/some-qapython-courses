import pytest
import re
from client.client import MysqlClient


def pytest_configure(config):
    mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()
    mysql_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_client.create_table_mc_methods()
        mysql_client.create_table_mc_requests()
        mysql_client.create_table_mc_users_srverror()
        mysql_client.create_table_bgst_reqs_clienterrror()
    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MysqlClient:
    client = request.config.mysql_client
    yield client
    client.connection.close()

@pytest.fixture(scope='session')
def items_from_logs():
    parts = [
        r'(?P<host>\S+)',
        r'\S+',
        r'(?P<user>\S+)',
        r'\[(?P<time>.+)\]',
        r'"(?P<request>.+)"',
        r'(?P<status>[0-9]+)',
        r'(?P<size>\S+)',
        r'"(?P<referer>.*)"',
        r'"(?P<agent>.*)"',
    ]
    pattern = re.compile(r'\s+'.join(parts) + r'\s*\Z')
    items = []

    with open('homework6/access.log', 'r') as f:
        lines = f.readlines()
        for line in lines:
            m = pattern.match(line)
            items.append(m.groupdict())
        f.close()

    [item.pop(key) for key in ('user', 'time', 'referer', 'agent') for item in items]

    return items