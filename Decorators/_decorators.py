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
