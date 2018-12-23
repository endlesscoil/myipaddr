import redis


class RedisDatastore(object):
    def __init__(self, cfg):
        self._config = cfg
        self._address = cfg.redis_address
        self._port = cfg.redis_port
        self._db = cfg.redis_db

    def init(self):
        self._redis = redis.Redis(host=self._address, port=self._port, db=self._db)

    def set(self, field, value):
        self._redis.hset('ipaddress', field, value)

    def get(self, field):
        return self._redis.hget('ipaddress', field)
