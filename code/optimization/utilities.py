from functools import wraps
from test_functions import *

def check_bounds(x, y, xy_range):
    return( x < xy_range[0] and x > xy_range[1] and y < xy_range[2] and y > xy_range[3])

# class that tracks calls to functions, can be used for comparing optimization algorithm performance
class Counter(object):
    counts = {}

    @staticmethod
    def count(func):
        def wrapped(*args, **kwargs):
            if func.__name__ in Counter.counts.keys():
                Counter.counts[func.__name__] += 1
            else:
                Counter.counts[func.__name__] = 1
            return func(*args,**kwargs)
        return wrapped