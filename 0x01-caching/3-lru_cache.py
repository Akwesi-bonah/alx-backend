#!/usr/bin/env python3
""" LRUCache module """
from collections import OrderedDict
Base = __import__("base_caching").BaseCaching


class LRUCache(Base):
    """ Inherits from BaseCaching && Uses LRU caching algorithm """
    def __init__(self):
        """initialize cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Updates the cache_data with key and value """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        elif len(self.cache_data) + 1 > self.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD: {}".format(last_key))
        self.cache_data[key] = item

    def get(self, key):
        """Gets the value for the provided key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)