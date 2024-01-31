#!/usr/bin/env python3
""" FIFOCache module """
Base = __import__("base_caching").BaseCaching


class FIFOCache(Base):
    """ Inherits from BaseCaching && Uses FIFO caching algorithm """
    def __init__(self):
        """initialize cache"""
        super().__init__()

    def put(self, key, item):
        """ Updates the cache_data with key and value """
        if key is None or item is None:
            return
        self.cache_data.update({key: item})
        if len(self.cache_data) > self.MAX_ITEMS:
            List = [[i, self.cache_data[i]] for i in self.cache_data]
            rm = List[0][0]
            self.cache_data.pop(rm)
            print("DISCARD: {}".format(rm))

    def get(self, key):
        """Gets the value for the provided key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)