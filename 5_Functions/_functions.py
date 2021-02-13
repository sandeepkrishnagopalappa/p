import datetime
import time

def func():
    print('Hello world')

def greeting(name):
    print(f'Hello {name}')

def greet(name, age, pay):
    print(f'Hello {name} you are {age} years and you have {pay} pay')

# Calling func by positional arguments
greeting("Sandeep")

# Calling func by keyword arguments
greeting(name="Sandeep")

# Calling func by positional and keyword arguments
greet("Sandeep", age=26, pay=1000)

# Function with Default as well as Mandatory arguments
def hello(name, company='Unknown'):
    print(f'Hello {name} you work for {company} company')

def greet(name, debug=False):
    if debug:
        print('You called greet function')
    print(f'Hello {name}')

def greet(name, reverse=False):
    if reverse:
        print(f'Hello {name[::-1]}')
    else:
        print(f'Hello {name}')

# Positional Only and Keyword Only arguments.
def greet(name, /, *, age, pay):
    print(f'Hello {name} you are {age} years and you have {pay} pay')

# Positional variable arguments (*args)
# * is used to grab arbitary excess items!
def func(a, *args):
    print(a, args)

# Keyword variable arguments (**kwargs)
def func2(a, **kwargs):
    print(a, kwargs)

# Combining both
def anyargs(*args, **kwargs):
    print(args)     # Tuple
    print(kwargs)   # Dictionary

anyargs(1, 2, 3, fname='steve', lname='jobs')

def add(*args):
    total = 0
    for num in args:
        total = total + num
    return total

print(add())
print(add(1))
print(add(1, 2))
print(add(10, 30, 45))
print(add(1000, 46273, 84545, 9834958, 4587583))
nums = [1, 2, 3, 4]
print(add(*nums))


# Unpacking arguments
def greet(name, age, pay):
    print(f'Hello {name} you are {age} years and you have {pay} pay')

data = ['Steve', 26, 1000]

greet(data[0], data[1], data[2])
greet(*data)    # Equivelent to greet("Steve", 26, 1000)

d_data = {"name": "steve", "age": 26, "pay": 1000}
greet(d_data['name'], d_data['age'], d_data['pay'])
greet(**d_data)     # Equivelent to greet(name="Steve", age=26, pay=1000)

# Returning Multiple Values from a Function
def myfunc():
    return 1, 2, 3

a, b, c = myfunc()

# Passing function to another function. Functions as "First class" objects.
def _delay(_func, _time, *args, **kwargs):
    time.sleep(_time)
    print(args)
    print(kwargs)
    result = _func(*args, **kwargs)
    return result

# Default values are evaluated only once
age = 10
def myinfo(my_name, my_age=age):
    print(my_name, my_age)

print(myinfo('steve', my_age=50))      # Prints (steve, 50)
print(myinfo('steve'))      # Prints(steve, 10)
age = 20
print(myinfo('steve'))      # Prints (steve, 10)

# Default arguments are evaluated only ONCE
def fun(a, L=[]):
    """ L=[] in the function declaration makes Python essentially do this:
    > This function has a parameter named L its default argument is [],
        let's set this particular [] aside and use it anytime there's no parameter passed for L.
    > Every time the function is called, create a variable L, and assign it either
        the passed parameter or the value we set aside earlier """
    L.append(a)
    return L


def func(employees=[], dt=datetime.datetime.now()):
    print(employees, dt)
    time.sleep(1)


func()
func([1, 2])
func()
# ================================================================

# lambda expressions/functions
def add(a, b):
    return a+b

add = lambda a, b: a+b
