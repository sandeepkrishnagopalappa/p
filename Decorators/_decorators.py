import time
from functools import wraps, partial
from inspect import signature
from collections import defaultdict

# Decoretors:

# A Decorator is a function that creates a wrapper around another function
# The wrapper is a new function that works exactly like a original function
# except that some kind of extra processing is carried out.
'''
First Class Functions are the one which is treated as any other object in Python like strings, lists dicts etc.
You can pass a function to another function, you can return a function from another function, just like any other functions.
A Decoretor is a function, which takes another function as an argument, adds some extra functisonality,
and returns another function without altering the source code of original function.
'''


def greet():
    print('Hello world')


def outer(some_function):   # Passing function as a parameter to other function
    some_function()


outer(greet)    # Prints Hello world


def print_after(seconds, func):     # Waits for 5 seconds and prints Hello world
    import time
    time.sleep(seconds)
    func()


print_after(5, greet)


def outer_function():
    def inner_function():
        print('Hello')
    return inner_function()     # executes the inner function


outer_function()


def outer_function():
    def inner_function():
        print('Hello')
    return inner_function     # Returns reference to the inner function waiting to be executed


f = outer_function()
f()


def outer(orig_func):
    # orig_func is the function to be wrapper
    def inner():
        print('Executing before original function')
        orig_func()
        print('Executing after original function')
    return inner


f = outer(greet)
f()


# =======================================================
def decorated_function(orig_function):
    def wrapper_function():
        print('Executed Before orig Function')
        return orig_function()
    return wrapper_function


@decorated_function
def show():
    print('Executing Show')


show()


# Logger Decorator
def logging(origfunc):
    def wrapper(*args, **kwargs):
        print('Calling function '+origfunc.__name__)
        return origfunc(*args, **kwargs)
    return wrapper


@logging
def add(a, b):
    print(a + b)


@logging
def sub(a, b):
    print(a - b)


@logging
def mul(a, b):
    print(a * b)


add(1, 2)
sub(2, 1)
mul(2, 2)


# =======================================================
# Calculates the execution time of the function
def timer(orig_func):
    def wrapper_func():
        start = time.time()
        orig_func()
        end = time.time()
        return end - start
    return wrapper_func


@timer
def test():
    print('Running test method')
    time.sleep(2.1)
    print('Hello world')
    

def wait(orig_function):
    def wrapper(*args):
        print(f'Waiting for element for 60 seconds')
        return orig_function(*args)
    return wrapper


@wait
def click_element(element_name):
    print(f'Clicked on element {element_name}')


@wait
def enter_text(element_name, text):
    print(f'editing {text} in {element_name} ')


# Preserve metadata such as the name, doc string, annotations, and calling signature are lost
# Logger Decorator
def logging(origfunc):
    @wraps(origfunc)
    def wrapper(*args, **kwargs):
        print('Calling function '+origfunc.__name__)
        return origfunc(*args, **kwargs)
    return wrapper


@logging
def add(a, b):
    """Adds two Numbers"""
    print(a + b)


print(add.__name__)     # Prints add
print(add.__doc__)      # Prints the doc string of the original function

# An important feature of the @wraps decorator is that it makes the wrapped function
# available to you in the __wrapped__ attribute. For example, if you want to access the
# wrapped function directly, you could do this

add = add.__wrapped__
add(1, 3)

# OR
add.__wrapped__(1, 2)

# Gaining direct access to the unwrapped function behind a decorator can be useful for
# debugging, introspection, and other operations involving functions. However, this
# recipe only works if the implementation of a decorator properly copies metadata using
# @wraps from the functools module


# Decorator with arguments
def debug(debug_mode):
    def decorate(func):
        def wrapper(*args, **kwargs):
            if not debug_mode:
                return func(*args, **kwargs)
            print('Executing method '+func.__name__ + ' in debug mode')
            return func(*args, **kwargs)
        return wrapper
    return decorate


@debug(False)    # The function is executed directly
def add(x, y):
    print(x + y)


@debug(True)  # The function is executed with debug message
def sub(x, y):
    print(x - y)


# Decorators with Default arguments
def logging(func=None, *, message='Hello'):
    if func is None:
        return partial(logging, message=message)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(message)
        func(*args, **kwargs)
    return wrapper


@logging        # add = logging(add)
def add(x, y):
    print(x + y)


@logging(message='Sub')     # add = logging(message='sub')(sub(x, y))
def sub(x, y):
    print(x - y)


add(1, 2)
sub(1, 2)


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError()
            return func(*args, **kwargs)
        return wrapper
    return decorate


# Class Decorators
def logger(cls):
    # cls is class
    for key, value in cls.__dict__.items():
        if callable(value):
            setattr(cls, key, logging(value))
    return cls


@logger     # Applies to all methods of the class
class Spam(object):

    def demo1(self):
        pass

    def demo2(self):
        pass

# Class decorators does not work on @classmethod and @staticmethod


# Write a Func Decorator that records the number of calls made on a function
def record(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        if not ((args, kwargs)) in wrapper.cache[func.__name__]:
            wrapper.cache[func.__name__].append((*args, kwargs))
        return func(*args, **kwargs)
    wrapper.count = 0
    wrapper.cache = defaultdict(list)
    return wrapper


# Class Decorator
class Record:
    def __init__(self, func):
        self.func = func
        self._count = 0

    def __call__(self, *args, **kwargs):
        self._count += 1
        return self.func(*args, **kwargs)

# Class Decorator with Arguments
class log:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('Calling')
            return func(*args, **kwargs)
        return wrapper