import miniupnpc


class UPNPProvider(object):
    def __init__(self, cfg):
        self._config = cfg

        self.init()

    def init(self):
        self._upnp = miniupnpc.UPnP()
        self._upnp.discoverdelay = 500
        self._upnp.discover()
        self._upnp.selectigd()

    def get_ip(self):
        return self._upnp.externalipaddress()
