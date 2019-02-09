# Simple Function with no arguments
def greet():
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


# Function with Default as well as Mandatory arguments
def hello(name, company='Unknown'):
    print(f'Hello {name} you work for {company} company')


hello('Steve', 'DXC')
hello('Steve')
hello(name='Steve', company='DXC')
hello(company='DXC', name='Steve')


# Variable number of Arguments
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


# Unpacking arguments
# def display_info(name, age, salary):    # Name of the arguments should be same as the key's of the dictionary
#     print(name, age, salary)

def display_info(*args, **kwargs):    # Name of the arguments should be same as the key's of the dictionary
    print(args, kwargs)


# * is used for unpacking list and tuple (positional arguments)
l_data = ['Mark', 26, 10000]
for item in l_data:
    display_info(*l_data)
    # display_info(l_data[0], l_data[1], l_data[2])

t_data = ('Mark', 26, 10000)
for item in t_data:
    display_info(*t_data)
    # display_info(t_data[0], t_data[1], t_data[2])


# ** is used for unpacking a dictionary (Keyword arguments)
d_data = [{'name': 'Mark', 'age': 26, 'salary': 10000},
          {'name': 'Steve', 'age': 27, 'salary': 20000}]
for d in d_data:
    display_info(**d)
    # display_info(d['name'], d['age'], d['salary'])
