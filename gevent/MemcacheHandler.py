from memcache.ttypes import *

class MemcacheHandler:
    def __init__(self):
        self._cache = {}

    def Set(self, key, value):
        self._cache[key] = value

    def MultiSet(self, data):
        self._cache.update(data)

    def Get(self, key):
        if key not in self._cache:
            return MemcacheGetResult(value='', found=False)
        return MemcacheGetResult(value=self._cache[key], found=True)

    def MultiGet(self, keys):
        return dict((key, self.Get(key)) for key in keys)

    def Delete(self, key):
        self._cache.pop(key, None)

    def MultiDelete(self, keys):
        for key in keys:
            self._cache.pop(key, None)
