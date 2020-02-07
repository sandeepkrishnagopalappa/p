from collections import defaultdict, Counter
from math import sqrt
import csv
from itertools import zip_longest
from itertools import chain
from functools import wraps

# Print total duplicates in the list
nums = [1, 2, 3, 1, 3, 5, 4, 3, 3, 1, 1, 1, 1]
duplicates = 0
for num in nums:
    if nums.count(num) > 1:
        duplicates += 1
print('Number of Duplicates ', duplicates)


# is_anagram
def is_anagram(word1: str, word2: str) -> bool:
    is_same_words = word1.lower() != word2.lower()
    has_same_letters = sorted(word1.lower()) == sorted(word2.lower())
    return has_same_letters and is_same_words


print(is_anagram('Listen', 'Silent'))   # Prints True
print(is_anagram('tea', 'eat'))     # Prints True
print(is_anagram('Bat', 'Pat'))     # Prints False


# Most common words
words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
        ]
words_count = Counter(words)
top_three = words_count.most_common(3)
print(top_three)


# Function that takes a sequence (like a list, string, or tuple)
# and a number n and returns the last n elements from the given sequence, as a list.

def lstrip(iterable, strip_value):
    """Return iterable with strip_value items removed from beginning."""
    stripped = []
    is_beginning = True
    for item in iterable:
        if is_beginning and item == strip_value:
            continue
        is_beginning = False
        stripped.append(item)
    return stripped


numbers = [1, 1, 1, 2, 1, 3, 4]

print(lstrip(numbers, 1))


# ===============================================================
# Removing duplicates from the list
def uniques_only(iterable):
    seen = set()
    i_nums = iter(iterable)
    for item in i_nums:
        if item not in seen:
            seen.add(item)
    return seen


print(uniques_only(numbers))

squares = (number ** 2 for number in numbers)

print(uniques_only(squares))

# ===============================================================


# Sorting the iterable if it is unhashable
def uniques_only(iterable, key=lambda item: item):
    seen = set()
    for item in iterable:
        val = item if key is None else key(item)
        if val not in seen:
            seen.add(val)
            yield item


d = [{'fname': 'steve', 'lname': 'jobs'},
     {'fname': 'bill', 'lname': 'gates'},
     {'fname': 'steve', 'lname': 'jobs'}
    ]

print(list(uniques_only(d, key=lambda dt: dt.get('fname'))))


# Sorting names list based on lastname
names = ['steve jobs', 'bill gates', 'larry ellison', 'john doe']
print(sorted(names, key=lambda name: name.split()[1]))

# Write function that takes a sequence (like a list, string, or tuple)
# and a number n and returns the last n elements from the given sequence, as a list.

# For Example :
# tail([1, 2, 3, 4, 5], 3) should return [3, 4, 5]
# tail('hello', 2) should return ['l', 'o']
# tail('hello', 0) should return []
def tail(iterable, n):
    if not isinstance(n, int):
        raise TypeError('Value of N should be Positive Integer')
    if n <=0:
        return []
    return list(iterable)[-n:]

#  Make a function that takes an iterable and a key function
#  and returns a dictionary of items grouped by the values returned
#  by the given key function.
def group_by(iterable, key_func=None):
    d = defaultdict(list)
    if key_func is None:
        for item in iterable:
            d[item].append(item)
        return d
    for item in iterable:
        d[key_func(item)].append(item)
    return d

# write a function, is_perfect_square, that accepts a number
# and returns True if it's a perfect square and False if it's not.
def is_perfect_square(number):
    return int(number) == int(sqrt(number) ** 2)

# write a function called csv_columns that accepts a file object and returns
# a dictionary mapping CSV headers to column data for each header.
def csv_columns(filename, *, headers=None, missing=None):
    rows = csv.reader(filename)
    if headers is None:
        _headers = next(rows)
    else:
        _headers = headers
    d = defaultdict(list)
    for row in rows:
        for h, item in zip_longest(_headers, row, fillvalue=missing):
             d[h].append(item)
    return d

# Write a function that accepts two lists and returns a single list
# with each of the given items in the concatinated.

# e.g concat_iter([1, 2, 3, 4], [5, 6, 7, 8]) should return [1, 5, 2, 6, 3, 7, 4, 8]
def concat_iter(iterable1, iterable2):
    c = zip(iterable1, iterable2)
    return list(chain(*c))

# write a class called CyclicList which acts sort of like a list except that looping
# over it will result in an infinite loop, repeating the list items forever.
class CyclicList:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        while True:
            for item in self.iterable:
                yield item

    def __len__(self):
        return len(self.iterable)

    def __getitem__(self, n):
        return self.iterable[n]

    def __setitem__(self, n, value):
        self.iterable[n] = value
        return self.iterable

    def append(self, item):
        self.iterable.append(item)

    def pop(self, *args, **kwargs):
        return self.iterable.pop(*args, **kwargs)

# write a function called all_same, which accepts a sequence (e.g. a list or tuple)
# and returns True if all the items in the given sequence are the same
# e.g all_same([1, 1, 1]) should return True
# all_same([1, 0, 1]) should return False
# all_same([(1, 'a'), (1, 'a')]) should return True
# all_same([(1, 'a'), (1, 'b')]) should return False
def all_same(iterable):
    return True if len(set(iterable)) == 1 else False


def all_same(iterable):
    for item in iterable:
        if item != iterable[0]:
            return False
    return True

# write a decorator function that will record the number of times a function is called.
def record_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        if not (args, kwargs) in wrapper.cache[func.__name__]:
            wrapper.cache[func.__name__].append((*args, kwargs))
        return func(*args, **kwargs)
    wrapper.call_count = 0
    wrapper.cache = defaultdict(list)
    return wrapper

#  create a class called EasyDict which creates objects that can
#  use key lookups and attribute lookups interchangeably:

# e.g person = EasyDict({'name': "Steve", 'location': "USA"})
# person.name should print 'Steve'
# person['location'] should print 'USA'
class EasyDict:
    def __init__(self, _dict=None):
        if _dict is None:
            _dict = {}
        self.__dict__.update(_dict)

    def __getitem__(self, item):
        return self.__dict__[item]
