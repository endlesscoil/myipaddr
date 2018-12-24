import redis


class RedisNotifier(object):
    """ Publishes an event to Redis to signify an IP address change. """
    def __init__(self, cfg):
        """ Constructor

        :param cfg: Config object
        :type cfg: Config (namedtuple)
        """
        self._config = cfg
        self._address = cfg.redis_address
        self._port = cfg.redis_port
        self._db = cfg.redis_db

    def init(self):
        """ Initializes the Redis notifier.

        :return: None
        :rtype: None
        """
        self._redis = redis.Redis(host=self._address, port=self._port, db=self._db)

    def send(self, current_ip):
        """ Sends the notification to the Redis event queue.

        :param current_ip: Current IP address
        :type current_ip: str
        :return: None
        :rtype: None
        """
        self._redis.publish('ipaddress.change', current_ip)
