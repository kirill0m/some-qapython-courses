from urllib.parse import urljoin
import requests


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def request(self, method, location=None, headers=None, data=None, json=None, expected_status=200, params=None):
        url = self.base_url if location is None else urljoin(self.base_url, location)

        response = requests.request(method=method,
                                    url=url,
                                    headers=headers,
                                    data=data,
                                    json=json,
                                    params=params)

        if expected_status is not None and response.status_code != expected_status:
            raise ResponseStatusCodeException

        return response

    def create_user(self, name):
        location = '/add_user'
        resp = self.request('POST',
                            location=location,
                            json={name[0]: name[1]},
                            expected_status=201)
        return resp
