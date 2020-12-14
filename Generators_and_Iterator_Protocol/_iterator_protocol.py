# Iterable:

"""
1. Anything that can be iterated or looped over is called iterable in Python.
2. All iterables have a special method call __iter__
3. String's, List's, Tuple's, Set's, Dictionary's, file objects and generator's are iterables.
4. All iterables can be passed to the built-in iter() function to get an iterator from them.
5. Any iterator can be passed to next() function to get the next item.
6. Iterators does not have length. They do not know how long they are.
7. Iterators do not have length can not be indexed. You can only call next() method to get the next item.
8. Generators are iterators, enumerate objects are iterators, zip function is an iterator file objects are iterators,
"""

# Iterators are Lazy Iterables. i.e. they dont determine what their next item is until you ask them for it

# Iterator Protocol
# Let's Consider a for Statement

# for item in obj:
    # Statements

# What happens under the Covers?
#     _iter = obj.__iter__()  # Get iterator object
#     while True:
#         try:
#             x = _iter.__next__()  # Get next item
#         except StopIteration:  # No more items
#             break
        # statements ...

# All the objects that work with the for-loop implement this low-level iteration protocol.
x = [1, 2, 3]
it = x.__iter__()
print(it.__next__())    # Manually Iterate over


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


# if you’re using next() manually,
# you can also instruct it to return a terminating value, such as None
def print_each2(iterable):
    while True:
        my_line = next(iterable, None)
        if line is None:
            break
        print(my_line)


def print_each(iterable):
    for item in iterable:     # This for loop is equivallent to the above custom iterator logic
        print(item)


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
        self.data = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data)


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


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        value = 0
        while value < self.start:
            yield value
            value += 1

    def __reversed__(self):
        while self.start > 0:
            yield self.start
            self.start -= 1
