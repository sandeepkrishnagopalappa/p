import time

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


# Function Decorator
# def _wait(orignal_function):
#     def wrapper(*args, **kwargs):
#         timeout = kwargs.get('timeout', orignal_function.__defaults__[0])
#         print(f'Waiting for element visibility for {timeout} seconds')
#         return orignal_function(*args, **kwargs)
#     return wrapper


# class FrameworkUtility:
#     def __init__(self, driver):
#         self.driver = driver
#
#     @_wait
#     def click_element(self, webelement, timeout=60):
#         print(f'Clicked on element {webelement}')
#
#     @_wait
#     def enter_text(self, webelement, value, timeout=60):
#         print(f'Entered text {value} in {webelement}')
#
#     @_wait
#     def select_item(self, webelement, item, timeout=60):
#         print(f'Selected item {item} from {webelement} list box')
#
#
# f = FrameworkUtility('driver')
# f.click_element('Submit')
# f.click_element('Login', timeout=100)
# f.select_item('City', 'Bangalore', timeout=20)
# f.enter_text('Username', 'user1')
