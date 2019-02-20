# Iterable:

'''
Anything that can be iterated or looped over is called iterable in Python.
All iterables have a special method call __iter__
String's, List's, Tuple's, Set's, Dictionary's, file's, generator's are iterables.
All iterables can be passed to the built-in iter function to get an iterator from them.
Any iterator can be passed to next() function to get the next item.
Iterators can not be indexed. You can only call next() method to get the next item.
Generators are iterators, enumerate objects are iterators, zip function is an iterator,
reversed(), file objects are iterators.
'''

# Iterators are Lazy. i.e. they dont determine what their next item is until you ask them for it

my_list = iter([1, 2, 3, 4])
print(type(my_list))    # Iterator object

my_set = iter({1, 1, 1, 2, 3, 4, 5})
print(type(my_set))     # Iterator object

my_dict = iter({'fname': 'test', 'lname': 'user'})
print(type(my_dict))    # Iterator object

my_string = iter('hello world')
print(type(my_string))      # Iterator object

my_tuple = iter((0, 1, 2, 3, 4, 5))
print(type(my_tuple))   # Iterator object


# Creating Custom iterators. The standard 'for' loop in Python, uses below logic for looping
def print_each(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break   # All elements in the iterable are exhausted
        else:
            print(item)


print_each(my_list)
print_each(my_set)
print_each(my_string)
print_each(my_dict)
print_each(my_tuple)


def print_each(iterable):
    for item in iterable:     # This for loop is equivallent to the above custom iterator logic
        print(item)


print_each(my_list)
print_each(my_set)
print_each(my_string)
print_each(my_dict)
print_each(my_tuple)


# Custom Iterator Class
class MyRange:
    """Iterator for looping over in forward direction"""
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        currentvalue = self.value
        self.value += 1
        return currentvalue


nums = MyRange(0, 100)


for num in nums:
    print(num)


# Custom Iterator
class MyItr:
    """Iterator for looping over a sequence in forward direction."""
    def __init__(self, iterable):
        self.index = 0
        self.data = iterable

    def __iter__(self):
        return self

    def __next__(self):

        if self.index > len(self.data)-1:
            raise StopIteration
        else:
            item = self.data[self.index]
            self.index += 1
            return item


num = MyItr([1, 2, 3, 4, 5])
_list = MyItr(['apple', 'google', 'yahoo', 'facebook'])
string = MyItr('spam')

for n in num:
    print(n)

for l in _list:
    print(l)

for s in string:
    print(s)


# Reverse Iterator
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, iterable):
        self.index = len(iterable) - 1
        self.data = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        else:
            item = self.data[self.index]
            self.index -= 1
            return item

        
rev_num = Reverse([1, 2, 3, 4, 5])
rev_list = Reverse(['apple', 'google', 'yahoo', 'facebook'])
rev_string = Reverse('spam')


for n in rev_num:
    print(n)

for l in rev_list:
    print(l)

for s in rev_string:
    print(s)
    
with open('words.txt') as file:
    text = file.readlines()

# Prints all the lines in text file in reverse order
rev_line = Reverse(text)

for line in rev_line:
    print(line, end='')
