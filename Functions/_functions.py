# Simple Function with no arguments
def greet():
    # Doc String
    """greet function prints hello world to the console"""
    print('Hello world')


# Function with argument
def show(name):
    print(f'Hello {name} welcome to Python!')


show('Steve')


# Function with return value
def display(name):
    return f'Hello {name} welcome to Python!'


print(display('Steve'))


# Function with Default arguments
def get_gender(sex='Unknown'):
    if sex.upper() == 'M':
        sex = 'Male'
    elif sex.upper() == 'F':
        sex = 'Female'
    print(sex)


get_gender('m')
get_gender('F')
get_gender()


def to_fahrenheit(temp):
    return round((temp * 1.8) + 32)


temperatures = [('Bangalore', 25), ('Chennai', 35), ('Delhi', 40), ('kolkata', 37)]
d_temp = {city: to_fahrenheit(temperature) for city, temperature in temperatures}
print(d_temp)


# Function with Default as well as Mandatory arguments
def hello(name, company='Unknown'):
    print(f'Hello {name} you work for {company} company')


hello('Steve', 'DXC')
hello('Steve')
hello(name='Steve', company='DXC')
hello(company='DXC', name='Steve')


# Function Annotations:
# Function annotations are usually used for type hints:
# for example, this function is expected to take two int arguments and is also expected to have an int return value:
def sum_two_numbers(a: int, b: int) -> int:
    return a + b


# ================================================================================================
# Variable number of Arguments
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
# def display_info(name, age, salary):    # Name of the arguments should be same as the key's of the dictionary
#     print(name, age, salary)

def display_info(*args, **kwargs):    # Name of the arguments should be same as the key's of the dictionary
    print(args, kwargs)


# ** is used for unpacking a dictionary (Keyword arguments)
d_data = [{'name': 'Mark', 'age': 26, 'salary': 10000},
          {'name': 'Steve', 'age': 27, 'salary': 20000}]
for d in d_data:
    display_info(**d)
    # display_info(d['name'], d['age'], d['salary'])


names = ['Steve', 'Mark']
info = {'age': 26, 'company': 'Apple'}

display_info(*names, **info)


# Attaching Informational Metadata to Function Arguments
def add(x: int, y: int) -> int:
    return x + y


# Returning Multiple Values from a Function
def myfunc():
    return 1, 2, 3


a, b, c = myfunc()


# Default values are evaluated only once
age = 10


def myinfo(my_name, my_age=age):
    print(my_name, my_age)


print(myinfo('steve', my_age=50))      # Prints (steve, 50)
print(myinfo('steve'))      # Prints(steve, 10)
age = 20
print(myinfo('steve'))      # Prints (steve, 10)
