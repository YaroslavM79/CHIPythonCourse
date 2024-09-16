import os

from dotenv import dotenv_values
from dotenv import load_dotenv

from .base_config_manager import BaseConfigManager

CONFIG_NAME = '.env'

__all__ = ['DotenvManager']


class DotenvManager(BaseConfigManager):

    def __init__(self):
        super(DotenvManager, self).__init__()

    def load(self):
        project_base_dir = os.getcwd()
        load_dotenv()
        self._keys = dotenv_values(os.path.join(project_base_dir, CONFIG_NAME))

    def value(self, key_name=None):
        return self._keys.get(key_name)
