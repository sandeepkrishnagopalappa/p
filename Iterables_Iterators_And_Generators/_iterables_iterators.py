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


# Creating Custom iterators. The standar 'for' loop in Python, uses below logic for looping
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
    def __init__(self, iterable):
        self.start = 0
        self.end = len(iterable)-1
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):

        if self.start > self.end:
            raise StopIteration
        else:
            item = self.iterable[self.start]
            self.start += 1
            return item

