from memcache.ttypes import *
import threading

class CacheShard:
    def __init__(self):
        self._lock = threading.Lock()
        self._dict = {}

    def set(self, key, value):
        with self._lock:
            self._dict[key] = value

    def update(self, data):
        with self._lock:
            self._dict.update(data)

    def get(self, key):
        return self._dict.get(key)

    def pop(self, key):
        with self._lock:
            self._dict.pop(key)

    def purge(self, keys):
        with self._lock:
            for key in keys:
                self._dict.pop(key)

    def stats(self):
        size = len(self._dict)
        mem = sum(len(key) + len(value) for key, value in self._dict.iteritems())
        return MemcacheStats(size=size, mem=mem)


class Cache:
    def __init__(self, shards):
        self._shards = shards
        self._shardMap = [CacheShard() for i in range(self._shards)]

    def _shardID(self, key):
        return hash(key) % self._shards

    def _shard(self, key):
        return self._shardMap[self._shardID(key)]

    def set(self, key, value):
        self._shard(key).set(key, value)

    def update(self, data):
        data_by_shard = {}
        for key, value in data.iteritems():
            shard_data = data_by_shard.setdefault(self._shardID(key), {})
            shard_data[key] = value
        for shard_id, shard_data in data_by_shard.iteritems():
            self._shard(shard_id).update(shard_data)

    def get(self, key):
        return self._shard(key).get(key)

    def pop(self, key):
        self._shard(key).pop(key)

    def purge(self, keys):
        keys_by_shard = {}
        for key in keys:
            shard_keys = keys_by_shard.setdefault(self._shardID(key), [])
            shard_keys.append(key)
        for shard_id, shard_keys in keys_by_shard:
            self._shard(shard_id).purge(shard_keys)

    def stats(self):
        all_stats = MemcacheStats(size=0, mem=0)
        for shard in self._shardMap:
            shard_stats = shard.stats()
            all_stats.size += shard_stats.size
            all_stats.mem += shard_stats.mem
        return all_stats


class MemcacheHandler:
    def __init__(self):
        self._cache = Cache(8)

    def Set(self, key, value):
        self._cache.set(key, value)

    def MultiSet(self, data):
        self._cache.update(data)

    def Get(self, key):
        return MemcacheGetResult(value=self._cache.get(key))

    def MultiGet(self, keys):
        return dict((key, self.Get(key)) for key in keys)

    def Delete(self, key):
        self._cache.pop(key)

    def MultiDelete(self, keys):
        self._cache.purge(keys)

    def Stats(self):
        return self._cache.stats()
