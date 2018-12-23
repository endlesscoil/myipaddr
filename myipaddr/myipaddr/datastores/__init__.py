from .redis_datastore import RedisDatastore


_datastores = {
    'redis': RedisDatastore
}


def get_datastore(cfg):
    cls = _datastores.get(cfg.datastore, None)
    if not cls:
        raise ValueError(f'Unknown datastore: {cfg.datastore}')

    instance = cls(cfg)
    instance.init()

    return instance
