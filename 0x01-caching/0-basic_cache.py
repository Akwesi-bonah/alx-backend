#!/usr/bin/env python3
""" BasicCache model """
BaseCache = __import__("base_caching").BaseCaching


class BasicCache(BaseCache):
    """ Inherits from BaseCaching """

    def __init__(self):
        """initializes the class"""
        super().__init__()

    def put(self, key, item):
        """ Adds item to cache"""
        if key is None or item is None:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """ Retrns the value related to a key """
        return self.cache_data.get(key)