import time

from myipaddr.config import load_config
from myipaddr.providers import get_provider
from myipaddr.notifiers import create_notifiers, send_notification
from myipaddr.datastores import get_datastore

CONFIG_FILE = 'myipaddr/myipaddr.json'


def main():
    cfg = load_config(CONFIG_FILE)
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
