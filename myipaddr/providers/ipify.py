import requests


class IpifyProvider(object):
    def __init__(self, cfg):
        self.config = cfg

    def init(self):
        pass

    def get_ip(self):
        return requests.get('https://api.ipify.org').text
