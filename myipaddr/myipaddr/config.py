import json
from collections import namedtuple


def load_config(config_path):
    config = None

    with open(config_path) as cfgfile:
        cfg = json.load(cfgfile)

        Config = namedtuple('Config', [
            'redis_address',
            'redis_port',
            'sleeptime',
            'provider',
            'redis_db',
            'pushover_apikey',
            'pushover_userkey',
            'notifiers',
            'datastore'
        ])
        config = Config(**cfg)

        assert (config.provider in ['ipify', 'upnp'])

    return config
