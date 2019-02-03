from itertools import count

'''
A Generator is a function that returns an iterator. It generates values using the 'yield' keyword.
when called on next() function a raises StopIteration exception when there are no more values to generate.
'yield' keyword suspends or pauses the execution of the function. But 'return' statement ends the function.
'''

# Looping
fruits = ['apple', 'orange', 'banana', 'strawberry']

# Traditional way of Looping..
for i in range(len(fruits)):
    print(fruits[i])

# Looping to get both the index and item
for index in range(len(fruits)):
    print(index, fruits[index])

# PYTHONIC approach
for fruit in fruits:
    print(fruit)

# To get both index and item (PYTHONIC approach)
for index, fruit in enumerate(fruits):
    print(index, fruit)
# ============================================


# Traditional way of getting even numbers
def get_even_numbers(stream):
    list_even = []
    for num in stream:
        if num % 2 == 0:
            list_even.append(num)
    return list_even


# list_evens = get_even_numbers(count())    # Infinite Loop [0, 1, 2, 3, 4..............]


# Using Generators (PYTHONIC approach)
def even_numbers(stream):
    for num in stream:
        if num % 2 == 0:
            yield num


my_nums = list(range(0, 10))
# We can iterate over the loop
for my_num in even_numbers(my_nums):
    print(my_num)

gen_even = even_numbers(count())    # Lazy .. [0, 1, 2, 3, 4..............]
print(next(gen_even))
print(next(gen_even))
print(next(gen_even))


# Produces squares of the number (Using Generators)
def square_numbers(stream):
    for num in stream:
        yield num ** 2


nums = [1, 2, 3, 4, 5, 6, 7]
n = square_numbers(nums)
print(next(n), end=',')
print(next(n), end=',')
print(next(n), end=',')
print(next(n))

# Using for loop
for n in square_numbers(nums):
    print(n, end=',')
    

# Check if the Number is Prime or Not Traditional approach
def isprime(number):
    # return all(iterable % i for i in range(2, iterable))
    for i in range(2, number):
        if number % i == 0:
            return False
        return True


# Check if the Number is Prime or Not Using Generator expression
def isprime_gen(number):
    return all(number % i for i in range(2, number))


print(isprime_gen(100))


def actual_lines(any_iterable):
    for line in any_iterable:
        if not line.strip():
            continue
        if line.startswith('#'):
            continue
        yield line
# =========================================================


# Passing a file object to Generator
with open('words.txt') as file:
    for line in actual_lines(file):
        print(line, end='')

# Passing a List to Generator
names = ['apple', 'yahoo', '#google', 'gmail', '#facebook']
for name in actual_lines(names):
    print(name)

# Passing a string object to Generator
my_string = 'abcd#xyz'
for c in actual_lines(my_string):
    print(c, end='')

# Passing a dictionary object to Generator
my_dict = {'fname': 'steve', 'lname': 'jobs', '#company': 'apple'}
for d in actual_lines(my_dict):
    print(d)
# =========================================================


# Custom Generator  # Generates Integers. One value at a time
def my_generator():
    item = 0
    while True:
        item += 1
        yield item


my_nums = my_generator()
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
