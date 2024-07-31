import os

from .config_manager_types import CliManager
from .config_manager_types import DotenvManager

__all__ = ['ConfigManager']

MANAGERS = {
    'dotenv': DotenvManager,
    'cli': CliManager,
}


class ConfigManagerSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(ConfigManagerSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ConfigManager:
    _manager = None
    __metaclass__ = ConfigManagerSingleton

    def __init__(self):
        self.load()

    @classmethod
    def load(cls):
        """
        load all variables from various source
        source can be:
        dotenv if set up --use_dotenv in command line
        variables in command line will be used if --use_dotenv not specified in command line
        :return:
        """
        manager_type = 'cli' if os.environ.get('APP_SETTINGS') else 'dotenv'
        ConfigManager._manager = MANAGERS.get(manager_type)()
        cls.init_fields()

    @classmethod
    def value(cls, key_name=None):
        return cls._manager.value(key_name=key_name)

    @classmethod
    def init_fields(cls):
        for key, value in cls._manager.keys.items():
            setattr(cls, key.lower(), value)
