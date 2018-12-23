import json
import time
from collections import namedtuple

from providers import get_provider
from notifiers import get_notifier
from datastores import get_datastore

CONFIG_FILE = 'myipaddr/myipaddr.json'


def load_config():
    config = None

    with open(CONFIG_FILE) as cfgfile:
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

def create_notifiers(cfg):
    notifiers = []

    for n in cfg.notifiers:
        notifiers.append(get_notifier(cfg, n))

    return notifiers

def send_notification(notifiers, current_ip):
    for n in notifiers:
        n.send(current_ip)

def main():
        cfg = load_config()

        datastore = get_datastore(cfg)
        provider = get_provider(cfg)
        notifiers = create_notifiers(cfg)

        while True:
            last_ip = datastore.get('current')
            current_ip = provider.get_ip()

            if current_ip != last_ip:
                print(f'IP address change: {last_ip} -> {current_ip}')

                datastore.set('current', current_ip)
                send_notification(notifiers, current_ip)

            time.sleep(cfg.sleeptime)


if __name__ == '__main__':
    main()
