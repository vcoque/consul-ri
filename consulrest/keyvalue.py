import json
import re
import requests

class KeyValue(object):

    def __init__(self, url):
        self._url = "%s/kv" % url

    def _get(self, key, recurse=None, keys=None):
        url = self._url + '/' + key

        params = dict()
        if recurse is not None:
            params['recurse'] = True
        if keys is not None:
            params['keys'] = True

        r = requests.get(url, params=params)

        if r.status_code == 200:
            return json.loads(r.text)
        else:
            return None

    def get(self, key, recurse=None):
        return self._get(key, recurse=recurse)

    def list(self, key=''):
        return self._get(key, keys=True)

    def set(self, key, value):
        r = requests.put(self._url + '/' + key, data=value)
        if r.status_code == 200 and re.match(r"true", r.text) is not None:
            return True
        else:
            return False

    def delete(self, key, recurse=None):
        url = self._url + '/' + key

        params = dict()
        if recurse is not None:
            params['recurse'] = True
        requests.delete(url, params=params)
