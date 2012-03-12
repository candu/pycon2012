struct MemcacheGetResult {
    1: optional string value,
}

service MemcacheService {
    void Set(1: string key, 2: string value),
    void MultiSet(1: map<string, string> data),
    MemcacheGetResult Get(1: string key),
    map<string, MemcacheGetResult> MultiGet(1: list<string> keys),
    void Delete(1: string key),
    void MultiDelete(1: list<string> keys)
}
