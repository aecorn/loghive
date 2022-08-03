import toml

def chosen_plugins_from_config():
    config = toml.load("plugins/plugin_config.toml")
    for area, plugin in config.items():
        print(f'Loading {plugin} as {area}')
        # Load plugin
        #import sqlalchemy_storage.sqlalchemy_storage

chosen_plugins_from_config()