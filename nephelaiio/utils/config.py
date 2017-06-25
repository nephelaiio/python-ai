from logging import getLogger

from anyconfig import load, merge, MS_REPLACE
from pkg_resources import resource_stream

_config_filename = 'nephelaiio.yml'
_config_defaults = resource_stream(__name__, _config_filename)
_config_search = [f"~/.{_config_filename}", f"./.{_config_filename}"]


def init_config():
    getLogger(__name__).debug('Loading default configuration')
    cfg = load(_config_defaults,
               ignore_missing=False)
    getLogger(__name__).debug(f"Loading user configuration overrides {' '.join(_config_search)}")
    user_config = load(_config_search,
                       ac_merge=MS_REPLACE,
                       ignore_missing=True)
    merge(cfg, user_config)
    getLogger(__name__).debug(f"Configuration complete, dumping value")
    getLogger(__name__).debug(cfg)
    return cfg
