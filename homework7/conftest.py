import os
import signal
import subprocess
import time
from copy import copy
import requests
from requests.exceptions  import ConnectionError
import pytest
import settings
from client import ApiClient

@pytest.fixture(scope='session')
def client():
    client = ApiClient(f'http://{settings.APP_HOST}:{settings.APP_PORT}')
    return client

def wait_ready(host, port):
    started = False
    st = time.time()
    while time.time() - st <= 15:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError(f'{host}:{port} did not started in 5s!')

def pytest_configure(config):
    if not hasattr(config, 'workerinput'):

        #app configuration
        app_path = os.path.join(os.path.abspath(os.path.join(__file__, os.pardir)), 'application', 'app.py')
        env = copy(os.environ)
        env.update({
            'APP_HOST': settings.APP_HOST,
            'APP_PORT': settings.APP_PORT,
            'MOCK_HOST': settings.MOCK_HOST,
            'MOCK_PORT': settings.MOCK_PORT
        })

        app_stderr = open('/tmp/app_stderr', 'w')
        app_stdout = open('/tmp/app_stdout', 'w')

        config.app_proc = subprocess.Popen(['python3.9',
                                            app_path],
                                           stderr=app_stderr,
                                           stdout=app_stdout,
                                           env=env)
        wait_ready(settings.APP_HOST, settings.APP_PORT)

        config.app_stderr = app_stderr
        config.app_stdout = app_stdout

        #mock configuration
        from mock import flask_mock
        flask_mock.run_mock()
        wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)


def pytest_unconfigure(config):
    #app unconfiguration
    config.app_proc.send_signal(signal.CTRL_C_EVENT)
    exit_code = config.app_proc.wait()

    assert exit_code == 0, f'app exited abnormally with exit code: {exit_code}'

    config.app_stderr.close()
    config.app_stdout.close()

    #mock unconfiguration
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')


