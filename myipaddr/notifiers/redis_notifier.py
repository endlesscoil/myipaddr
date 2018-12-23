import redis


class RedisNotifier(object):
    def __init__(self, cfg):
        self._config = cfg
        self._address = cfg.redis_address
        self._port = cfg.redis_port
        self._db = cfg.redis_db

    def init(self):
        self._redis = redis.Redis(host=self._address, port=self._port, db=self._db)

    def send(self, current_ip):
        self._redis.publish('ipaddress.change', current_ip)
