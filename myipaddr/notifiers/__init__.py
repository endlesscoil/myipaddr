from .pushover_notifier import PushoverNotifier
from .redis_notifier import RedisNotifier


_notifiers = {
    'pushover': PushoverNotifier,
    'redis': RedisNotifier,
}


def get_notifier(cfg, notifier):
    cls = _notifiers.get(notifier)
    if not cls:
        raise ValueError(f'Unknown notifier: {notifier}')

    instance = cls(cfg)
    instance.init()

    return instance
