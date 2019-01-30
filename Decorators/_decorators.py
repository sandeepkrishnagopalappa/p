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


names = ['sandeep', 'steve', 'jack']
print(to_upper(names))

print(random_choice())
print(random_choice_1('Hi'))


# Class Decorator
class Wait_Element_Visibility:
    def __init__(self, original_function):
        self.orignal_function = original_function

    def __call__(self, *args, **kwargs):
        print(kwargs)
        if self.orignal_function.__name__ == 'click_element':
            if not kwargs.get('timeout'):
                default_timeout = self.orignal_function.__defaults__[-1]
                print(f'Waiting for Element to be clickable for {default_timeout} seconds')
            else:
                print('Waiting for Element to be editable for seconds', kwargs.get('timeout'))
        elif self.orignal_function.__name__ == 'enter_text':
            if not kwargs.get('timeout'):
                default_timeout = self.orignal_function.__defaults__[-1]
                print(f'Waiting for Element to be editable for {default_timeout} seconds')
        elif self.orignal_function.__name__ == 'select_item':
            print('Waiting for element to be selectable')
            if not kwargs.get('timeout'):
                default_timeout = self.orignal_function.__defaults__[-1]
                print(f'Waiting for Element to be selectable for {default_timeout} seconds')
        self.orignal_function(self, *args, **kwargs)


# Function Decorator
def dec_wait_element_visibility(orignal_function):
    def wrapper(*args, **kwargs):
        if not kwargs.get('timeout'):
            wait_element_visibility(args, orignal_function.__defaults__[-1])
        return orignal_function(*args, **kwargs)
    return wrapper


def wait_element_visibility(webelement, timeout):
    print(f'Waiting for element visibility {webelement} for {timeout}')


@dec_wait_element_visibility
def click_element(webelement, timeout=60):
    print('Clicking on Element')


click_element('Login')


class framework_utility:
    def __init__(self, driver):
        self.driver = driver

    @Wait_Element_Visibility
    def click_element(self, webelement=None, timeout=60):
        pass

    @Wait_Element_Visibility
    def enter_text(self, webelement=None, value=None, timeout=60):
        pass

    @Wait_Element_Visibility
    def select_item(self, webelement=None, item=None, timeout=60):
        pass


f = framework_utility('driver')
f.click_element('Login', timeout=100)
f.select_item('City', 'Bangalore', timeout=20)
f.enter_text('Username', 'user1')

