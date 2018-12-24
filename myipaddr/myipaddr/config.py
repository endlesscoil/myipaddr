import json
from collections import namedtuple


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


def load_config(config_path):
    """ Load configuration data from the specified JSON file.

    :param config_path: Path to config file
    :type config_path: str
    :return: Configuration object
    :rtype: Config (namedtuple)
    """
    config = None

    with open(config_path) as cfgfile:
        cfg = json.load(cfgfile)
        config = Config(**cfg)

        assert config.provider in ['ipify', 'upnp']
        assert config.datastore == 'redis'

    return config
