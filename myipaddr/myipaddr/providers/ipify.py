import requests

IPIFY_URL = 'https://api.ipify.org'


class IpifyProvider(object):
    """ Provides an interface for Ipify in order to retrieve the external IP address. """
    def __init__(self, cfg):
        """ Constructor

        :param cfg: Config object
        :type cfg: Config (namedtuple)
        """
        self.config = cfg

    def init(self):
        """ Initializes the provider for use.

        :return: None
        :rtype: None
        """
        pass

    def get_ip(self):
        """ Retrieves the current external IP address.

        :return: ip address
        :rtype: str
        """
        return requests.get(IPIFY_URL).text
