#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exer').Cache

cache = Cache()
#-----task 0,1-----------
# data = b"hello"
# key = cache.store(data)
# print(key)

# local_redis = redis.Redis()
# print(local_redis.get(key))
#-----task2-----------
# cache.store(b"first")
# print(cache.get(cache.store.__qualname__))

# cache.store(b"second")
# cache.store(b"third")
# print(cache.get(cache.store.__qualname__))
#-----task3-----------
# s1 = cache.store("first")
# print(s1)
# s2 = cache.store("secont")
# print(s2)
# s3 = cache.store("third")
# print(s3)

# inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
# outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

# print("inputs: {}".format(inputs))
# print("outputs: {}".format(outputs))

#-----task4-----------
#from cache import Cache, call_history, replay

cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)