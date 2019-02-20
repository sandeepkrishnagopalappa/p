import time
import random

# Decoretors:
'''
First Class Functions are the one which is treated as any other object in Python like strings, lists dicts etc.
You can pass a function to another function, you can return a function from another function, just like any other functions.
A Decoretor is a function, which takes another function as an argument, adds some extra functisonality,
and returns another function without altering the source code of original function.
'''


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


# =======================================================
# Calculates the execution time of the function
def timer(orig_func):
    def wrapper_func():
        start = time.time()
        orig_func()
        end = time.time()
        return end - start
    return wrapper_func


def mapper(orig_fun):
    def wrapper(names):
        return [orig_fun(name) for name in names]
    return wrapper


# Parameterized Decorator
def power_of(exp=2):
    def exp_dig(orig_fun):
        def wrapper(*args, **kwargs):
            return orig_fun(*args, **kwargs) ** exp
        return wrapper
    return exp_dig


@power_of(2)
def random_choice():
    return random.choice([1, 3, 7, 4])


@power_of(3)
def random_choice_1(name):
    return random.choice([1, 3, 7, 4])


@mapper
def to_upper(s):
    return s.upper()


names = ['rob', 'steve', 'jack']
print(to_upper(names))

print(random_choice())
print(random_choice_1('Hi'))


# Function Decorator
def _wait(orignal_function):
    def wrapper(*args, **kwargs):
        timeout = kwargs.get('timeout', orignal_function.__defaults__[0])
        print(f'Waiting for element visibility for {timeout} seconds')
        return orignal_function(*args, **kwargs)
    return wrapper


class FrameworkUtility:
    def __init__(self, driver):
        self.driver = driver

    @_wait
    def click_element(self, webelement, timeout=60):
        print(f'Clicked on element {webelement}')

    @_wait
    def enter_text(self, webelement, value, timeout=60):
        print(f'Entered text {value} in {webelement}')

    @_wait
    def select_item(self, webelement, item, timeout=60):
        print(f'Selected item {item} from {webelement} list box')


f = FrameworkUtility('driver')
f.click_element('Submit')
f.click_element('Login', timeout=100)
f.select_item('City', 'Bangalore', timeout=20)
f.enter_text('Username', 'user1')
