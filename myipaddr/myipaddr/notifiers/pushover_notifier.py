from pushover import Client


class PushoverNotifier(object):
    """ Notifier class for Pushover """
    def __init__(self, cfg):
        """ Constructor

        :param cfg: Config object
        :type cfg: Config (namedtuple)
        """
        self._config = cfg
        self._apikey = cfg.pushover_apikey
        self._userkey = cfg.pushover_userkey

    def init(self):
        """ Initializes the notification.

        :return: None
        :rtype: None
        """
        self._client = Client(self._userkey, api_token=self._apikey)

    def send(self, current_ip):
        """ Sends the notification

        :param current_ip: Current IP address
        :type current_ip: str
        :return: None
        :rtype: None
        """
        self._client.send_message(f"New home IP address: {current_ip}")
