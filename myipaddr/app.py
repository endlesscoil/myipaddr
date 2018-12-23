import json
import time
from collections import namedtuple

import redis
from pushover import Client


CONFIG_FILE = 'myipaddr/myipaddr.json'


def getip_upnp(cfg):
    ret = None

    try:
        import miniupnpc

        upnp = miniupnpc.UPnP()
        upnp.discoverdelay = 500
        upnp.discover()
        upnp.selectigd()

        ret = upnp.externalipaddress().decode('utf-8')

    except:
        import traceback; traceback.print_exc()

    return ret

def getip_ipify(cfg):
    ret = None

    try:
        import requests

        ret = requests.get('https://api.ipify.org').text
    except:
        import traceback; traceback.print_exc()

    return ret

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
        ])
        config = Config(**cfg)

        assert (config.provider in ['ipify', 'upnp'])

    return config

def notify_pushover(cfg, current_ip):
    Client(cfg.pushover_userkey, api_token=cfg.pushover_apikey).send_message(f"New home IP address: {current_ip}")

def get_current_ip(cfg):
    current_ip = None

    if cfg.provider == 'upnp':
        current_ip = getip_upnp(cfg)
    elif cfg.provider == 'ipify':
        current_ip = getip_ipify(cfg)

    return current_ip

def send_notifications(_redis, cfg, current_ip):
    _redis.publish('ipaddress.change', current_ip)
    notify_pushover(cfg, current_ip)

def main():
        cfg = load_config()
        _redis = redis.Redis(host=cfg.redis_address, port=cfg.redis_port, db=cfg.redis_db)

        while True:
            last_ip = _redis.hget('ipaddress', 'current')
            current_ip = get_current_ip(cfg)

            if current_ip != last_ip:
                print(f'New IP address: {current_ip}')

                _redis.hset('ipaddress', 'current', current_ip)

                send_notifications(_redis, cfg, current_ip)

            time.sleep(cfg.sleeptime)


if __name__ == '__main__':
    main()
