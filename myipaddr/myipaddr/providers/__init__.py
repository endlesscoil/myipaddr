from .upnp import UPNPProvider
from .ipify import IpifyProvider


_providers = {
    'upnp': UPNPProvider,
    'ipify': IpifyProvider,
}


def get_provider(cfg):
    cls = _providers.get(cfg.provider, None)
    if not cls:
        raise ValueError(f'Unknown provider: {cfg.provider}')

    instance = cls(cfg)
    instance.init()

    return instance
