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


#METODOS PARA CRUD DE DEALS#
    def get_deals(self, deal_id=None, **kwargs):
        if deal_id is not None:
            url = "deals/{0}".format(deal_id)
        else:
            url = "deals"
        return self._get(url, **kwargs)

    def add_deal(self, **kwargs):
        url = "deals"
        if kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post(url, json=params)

    def update_deal(self, deal_id, **kwargs):
        if deal_id is not None and kwargs is not None:
            url = "deals/{0}".format(deal_id)
            params = {}
            params.update(kwargs)
            return self._put(url, json=params)

    def delete_deal(self, deal_id):
        if deal_id is not None:
            url = "deals/{0}".format(deal_id)
            return self._delete(url)

#METODOS PARA CRUD DE PERSONAS#
    def get_persons(self, person_id=None, **kwargs):
        if person_id is not None:
            url = "persons/{0}".format(person_id)
        else:
            url = "persons"
        return self._get(url, **kwargs)



    def add_person(self, **kwargs):
        if kwargs is not None:
            url = "persons"
            params = {}
            params.update(kwargs)
            return self._post(url, json=params)

    def update_person(self, data_id, **kwargs):
        if data_id is not None and kwargs is not None:
            url = "persons/{0}".format(data_id)
            params = {}
            params.update(kwargs)
            return self._put(url, json=params)

    def delete_person(self, data_id):
        if data_id is not None:
            url = "persons/{0}".format(data_id)
            return self._delete(url)
