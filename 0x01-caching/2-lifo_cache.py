#!/usr/bin/env python3
""" LIFOCache module """
from collections import OrderedDict
Base = __import__("base_caching").BaseCaching


class LIFOCache(Base):
    """ Inherits from BaseCaching && Uses LIFO caching algorithm """
    def __init__(self):
        """initialize cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Updates the cache_data with key and value """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > self.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Gets the value for the provided key"""
        return self.cache_data.get(key, None)