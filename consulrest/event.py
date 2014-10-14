import json
import requests

class Event(object):

    def __init__(self, url):
        self._url = "%s/event" % url

    def list(self, name=None):
        url = self._url + "/list"
        if name is not None:
            url += '?name=%s' % (name)

        r = requests.get(url)
        if r.ok
            return json.loads(r.text)

        r.raise_for_status()

    def fire(self, event, payload=None, node=None, service=None, tag=None):
        url = self._url + "/fire/" + event

        params = dict()
        if node is not None:
            params["node"] = node
        if service is not None:
            params["service"] = service
        if tag is not None:
            params["tag"] = tag

        r = requests.put(url, data=payload, params=params)
        if r.ok == 200:
            return json.loads(r.text)

        r.raise_for_status()
