import time
from functools import wraps, partial
import time
import csv
import tracemalloc

# Decorators:

# A Decorator is a function that creates a wrapper around another function
# The wrapper is a new function that works exactly like a original function
# except that some kind of extra processing is carried out.
'''
First Class Functions are the one which is treated as any other object in Python like strings, lists dicts etc.
You can pass a function to another function, you can return a function from another function, just like any other functions.
A Decoretor is a function, which takes another function as an argument, adds some extra functisonality,
and returns another function without altering the source code of original function.
'''


# Log Decorator
def logging(msg="Hello World", debug=True):
    def log(func):
        def wrapper(*args, **kwargs):
            if debug:
                print(msg, func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return log


# Delay Decorator
def _delay(_time_delay):
    def delay(func):
        def wrapper(*args, **kwargs):
            time.sleep(_time_delay)
            return func(*args, **kwargs)
        return wrapper
    return delay


# Repeats the function 'n' times
def _repeat(n):
    def repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return repeat


# Time Decorator
def _time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Exe Time for {func.__name__} : {end-start}')
        return result
    return wrapper


# Positive Decorator
def positive(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return abs(result)
    return wrapper


# Memory Decorator
def _memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        print(f"Memory Usage: {tracemalloc.get_traced_memory()}")
        tracemalloc.stop()
        return result
    return wrapper


# Counting Number of Function Calls.
def func_count(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


def type_check(exp_types, actual_values):
    for _type, _value in zip(exp_types, actual_values):
        if not isinstance(_value, _type):
            raise TypeError


# Decorator to Type Check.
def validate(**typs):
    def _validate(func):
        def wrapper(*args, **kwargs):
            _expected_types = list(typs.values())
            _actual_values = list(args)
            type_check(_expected_types, _actual_values)
            return func(*args, **kwargs)
        return wrapper
    return _validate


@_memory
def read_csv():
    with open('data/covid_data.csv') as f:
        records =[]
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append((row[2], row[3], row[5]))
        return records


@_memory
def test_list():
    a = []
    for i in range(1000000):
        a.append(i)
    return a


@_memory
def test_tuple():
    a = tuple(list(range(1000000)))
    return a


@validate(a=int, b=int)
def add(a, b):
    print("Executing Add")
    return a+b


@validate(a=int, b=int)
def sub(a, b):
    return a-b


@validate(name=str, age=int, pay=float)
def greet(name, age, pay):
    print(f"Hello {name} You are {age} years of age and you have {pay}")


# Class Decorator
class Record:
    def __init__(self, func):
        self.func = func
        self._count = 0

    def __call__(self, *args, **kwargs):
        self._count += 1
        return self.func(*args, **kwargs)
