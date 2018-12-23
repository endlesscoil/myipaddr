from pushover import Client


class PushoverNotifier(object):
    def __init__(self, cfg):
        self._config = cfg
        self._apikey = cfg.pushover_apikey
        self._userkey = cfg.pushover_userkey

    def init(self):
        self._client = Client(self._userkey, api_token=self._apikey)

    def send(self, current_ip):
        self._client.send_message(f"New home IP address: {current_ip}")
