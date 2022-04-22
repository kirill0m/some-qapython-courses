from urllib.parse import urljoin
import requests
from requests.cookies import cookiejar_from_dict


class ResponseStatusCodeException(Exception):
    pass


class CampaignNotFoundException(Exception):
    pass


class SegmentNotFoundException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url, login, password):
        self.base_url = base_url
        self.login = login
        self.password = password
        self.session = requests.Session()
        self.csrf_token = None
        self.headers = {
            'X-CSRFToken': None,
        }

    def _request(self, method, location=None, headers=None, data=None, json=None, expected_status=200, params=None):
        url = self.base_url if location is None else urljoin(self.base_url, location)

        response = self.session.request(method=method, url=url, headers=headers, data=data, json=json,
                                        params=params, allow_redirects=True)

        if expected_status is not None and response.status_code != expected_status:
            raise ResponseStatusCodeException

        return response

    def post_login(self):
        login_location = 'https://auth-ac.my.com/auth'

        data = {
            'email': f'{self.login}',
            'password': f'{self.password}',
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/',
        }

        headers = {
            'Referer': 'https://target.my.com/'
        }

        resp = self._request(method='POST', location=login_location, headers=headers, data=data)
        cookies_for_csrf = resp.request.headers['Cookie']
        cookies_for_csrf_list = cookies_for_csrf.split('; ')

        tokens = dict(zip([i.split('=')[0] for i in cookies_for_csrf_list],
                          [i.split('=')[-1] for i in cookies_for_csrf_list]))

        headers_for_csrf = {
            'Cookie': f'{cookies_for_csrf}'
        }

        csrf_resp = self._request(method='GET', location='csrf/', headers=headers_for_csrf)

        tokens['csrftoken'] = [i.split('=')[-1] for i in csrf_resp.headers['Set-Cookie'].split('; ') if 'csrftoken' in i][0]

        self.csrf_token = tokens['csrftoken']
        self.headers['X-CSRFToken'] = self.csrf_token
        self.session.cookies = cookiejar_from_dict(tokens)

        return resp

    def post_create_campaign(self, name, objective, package_id):
        location = 'api/v2/campaigns.json'
        json_data = {
            'name': name,
            'objective': objective,
            'package_id': package_id
        }
        resp = self._request(method='POST', location=location, json=json_data,
                             headers=self.headers)
        campaign_id = resp.json()['id']
        yield campaign_id
        self._delete_campaign_by_id(campaign_id)

    def get_campaign_by_id(self, id):
        location = 'api/v2/campaigns.json'
        resp = self._request(method='GET', location=location, headers=self.headers, params={'_q': id}).json()
        if resp['count'] > 0:
            return resp['items'][0]
        else:
            raise CampaignNotFoundException

    def _delete_campaign_by_id(self, id):
        location = f'api/v2/campaigns/{id}.json'
        data = {
            'status': 'deleted'
        }
        resp = self._request(method='POST', location=location, headers=self.headers, json=data, expected_status=204)
        return True if resp.ok else False


    def post_create_segment(self, name, pass_condition, relations, logic_type):
        location = 'api/v2/remarketing/segments.json'
        json_data = {
            "name": name,
            "pass_condition": pass_condition,
            "relations": [
                {
                    "object_type": relations['object_type'],
                    "params": {
                        "type": relations['param_type'],
                        "left": relations['param_left'],
                        "right": relations['param_right']
                    }
                }
            ],
            "logicType": logic_type
        }
        resp = self._request(method='POST', location=location, json=json_data,
                             headers=self.headers)
        segment_id = resp.json()['id']
        return segment_id

    def get_segment_by_id(self, id):
        location = 'api/v2/remarketing/segments.json'
        resp = self._request(method='GET', location=location, headers=self.headers, params={'fields': 'id,name',
                                                                                            '_id': id}).json()
        if resp['count'] != 0:
            return resp['items'][0]
        else:
            raise SegmentNotFoundException

    def delete_segment_by_id(self, id):
        if self.get_segment_by_id(id):
            location = 'api/v1/remarketing/mass_action/delete.json'
            json_data = [
                {
                    "source_id": id,
                    "source_type": "segment"
                }
            ]
            resp = self._request(method='POST', location=location, headers=self.headers, json=json_data)
            return True if len(resp.json()['successes']) > 0 else False
