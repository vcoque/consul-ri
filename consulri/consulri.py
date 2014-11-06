import event
import keyvalue

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8500
VERSION = 'v1'

class ConsulRI:

    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT):
        self._host = host
        self._port = port

        self._url = "http://%s:%s/%s" % (host, port, VERSION)
        self.kv = keyvalue.KeyValue(self._url)
        self.event = event.Event(self._url)
