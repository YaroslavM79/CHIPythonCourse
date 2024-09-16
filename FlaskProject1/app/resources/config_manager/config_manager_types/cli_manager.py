import argparse
import os

from .base_config_manager import BaseConfigManager

__all__ = ['CliManager']


class CliManager(BaseConfigManager):
    """
    Manage config values from command line.
    """

    def __init__(self):
        super(CliManager, self).__init__()

    def load(self):
        self._keys['APP_SETTINGS'] = os.environ['APP_SETTINGS']

    def value(self, key_name=None):
        return self._keys.get(key_name)

    def parser_args(self):
        parser = argparse.ArgumentParser()
        parser_args, _ = parser.parse_known_args()
        return parser_args
