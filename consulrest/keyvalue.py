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

        if r.ok:
            return json.loads(r.text)
        elif r.status_code == 404:
            return []
        else:
            r.raise_for_status()

    def get(self, key, recurse=None):
        return self._get(key, recurse=recurse)

    def list_keys(self, key=''):
        return self._get(key, keys=True)

    def set(self, key, value, cas=None):
        params = dict()
        if cas is not None:
            params['cas'] = cas

        r = requests.put(self._url + '/' + key, data=value, params=params)

        if r.ok:
            if re.match(r"true", r.text) is not None:
                return True
            elif re.match(r"false", r.text) is not None:
                return False
        else:
           r.raise_for_status()

    def delete(self, key, recurse=None):
        url = self._url + '/' + key

        params = dict()
        if recurse is not None:
            params['recurse'] = True
        r = requests.delete(url, params=params)
        r.raise_for_status()
