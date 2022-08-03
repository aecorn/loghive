import toml
from importlib import import_module, reload
import os

def chosen_plugins_from_config():
    config = toml.load("plugins/plugin_config.toml")
    for area, plugin in config.items():
        print(f'Loading {plugin} as {area}')
        # Load plugin
        mod = import_module(f'{plugin}.{plugin}')
        reload(mod)
        #print(mod.__dict__)
        main = getattr(mod, "plugin_main")
        main()

chosen_plugins_from_config()