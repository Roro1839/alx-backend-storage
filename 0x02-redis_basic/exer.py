#!/usr/bin/env python3
"""

"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """Tracks the number of calls made to a method in a Cache class.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Invokes the given method after incrementing its call counter"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    
    return wrapper

def call_history(method: Callable) -> Callable:
    """stores history of inputs and outputs of aparticular function"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """used to ensure that the wrapper function (wrapper)
        retains the original method's name, docstring, and other metadata
        """
        input_key = f"{key}:inputs"
        output_key = f"{key}:outputs"
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(output_key, output)
        return output
    return wrapper

def replay(fn: Callable) ->None:
    """display the history of calls of a particular function."""
    """stores history of inputs and outputs of aparticular function"""
    r = redis.Redis()
    function_name = fn.__qualname__
    value = r.get(function_name)
    try:
        value = int(value.decode("utf-8"))
    except Exception:
        value = 0
    
    print("{} was called {} times:".format(function_name, value))
    inputs = r.lrange("{}:inputs".format(function_name), 0, -1)

    outputs = r.lrange("{}:inputs".format(function_name), 0, -1)
    
    for input, output in zip(inputs, outputs):
        try:
            input = input.decode("utf-8")
        except Exception:
            input =""

        try:
            output = output.decode("utf-8")
        except Exception:
            output =""

        print("{}(*{}) -> {}".format(function_name, input, output))

replay(cache.store)

class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)


    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string."""
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(self, key: str,  fn: Callable = None) -> Union[str, bytes, int, float]:
        """ Takes a key string arg and an optional Callable args fn
        returns data back to the desired format
        """
        value = self._redis.get(key)
        """converts data back to the desired format"""
        if fn is None:
            return value
        return fn(value)

    def get_str(self, key: str) -> str:
        return self.get(key)

    def get_int(self, key: str) -> int:
        value = self.get(key)
        if value is None:
            return value
        return int(value)
