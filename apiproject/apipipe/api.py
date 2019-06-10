import requests
import json
from base64 import b64encode
from urllib.parse import urlencode


class ApiPipedrive:
    api_version = "v1/"
    header = {"Accept": "application/json, */*", "content-type": "application/json"}

    def __init__(self, api_base_url):
        self.api_base_url = api_base_url
        self.token = "9d3f3e7ab1582ac6331856daa24a3d0972f2c9fa"

    def make_request(self, method, endpoint, data=None, json=None, **kwargs):

        if self.token:
            url = '{0}{1}{2}?api_token={3}'.format(self.api_base_url, self.api_version, endpoint, self.token)
            if method == "get":
                response = requests.request(method, url, headers=self.header, params=kwargs)

            else:
                response = requests.request(method, url, headers=self.header, data=data, json=json)

            return response.json()
        else:
            raise Exception("TOKEN ERROR")

    def _get(self, endpoint, data=None, **kwargs):
        return self.make_request('get', endpoint, data=data, **kwargs)

    def _post(self, endpoint, data=None, json=None, **kwargs):
        return self.make_request('post', endpoint, data=data, json=json, **kwargs)

    def _delete(self, endpoint, **kwargs):
        return self.make_request('delete', endpoint, **kwargs)

    def _put(self, endpoint, json=None, **kwargs):
        return self.make_request('put', endpoint, json=json, **kwargs)
