import miniupnpc


class UPNPProvider(object):
    """ Provides an interface for UPNP in order to retrieve the external IP address. """
    def __init__(self, cfg):
        """ Constructor

        :param cfg: Config object
        :type cfg: Config (namedtuple)
        """
        self._config = cfg

        self.init()

    def init(self):
        """ Initializes the provider for use.  Discovers UPNP servers.

        :return: None
        :rtype: None
        """
        self._upnp = miniupnpc.UPnP()
        self._upnp.discoverdelay = 500
        self._upnp.discover()
        self._upnp.selectigd()

    def get_ip(self):
        """ Retrieves the current external IP address.

        :return: ip address
        :rtype: str
        """
        return self._upnp.externalipaddress()
