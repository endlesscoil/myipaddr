import redis


class RedisDatastore(object):
    """ Stores information about the external IP address inside of Redis """
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
        """ Initializes the datastore for use.  Creates the connection to Redis.

        :return: None
        :rtype: None
        """
        self._redis = redis.Redis(host=self._address, port=self._port, db=self._db)

    def set(self, field, value):
        """ Sets a field inside of our hash.

        :param field: Field name
        :type field: str
        :param value: Field value
        :type value: str
        :return: None
        :rtype: None
        """
        self._redis.hset('ipaddress', field, value)

    def get(self, field):
        """ Retrieves the field value from our hash.

        :param field: field name
        :type field: str
        :return: field value
        :rtype: str
        """
        val = self._redis.hget('ipaddress', field)
        if isinstance(val, bytes):
            val = val.decode('utf-8')

        return val
