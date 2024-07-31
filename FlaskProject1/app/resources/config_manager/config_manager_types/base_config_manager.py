from abc import ABCMeta, abstractmethod
from collections import defaultdict


class BaseConfigManager:
    __metaclass__ = ABCMeta

    def __init__(self):
        self._keys = defaultdict()
        self.load()

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def value(self, key_name=None):
        pass

    @property
    def keys(self):
        return self._keys
