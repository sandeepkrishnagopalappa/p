from itertools import groupby
import datetime
import collections

# Coding Problem-3 Print total duplicates in the list
nums = [1, 2, 3, 1, 3, 5, 4, 3, 3, 1, 1, 1, 1]
duplicates = 0
for num in nums:
    if nums.count(num) > 1:
        duplicates += 1
print('Number of Duplicates ', duplicates)


# Deleting Sequence
sequence = [1, 2, 1, 1, 1, 2, 3, 4, 2, 2]


def compact(iterable):
    return (item for item, group in groupby(iterable))    # Generator expression


a = compact(sequence)
print(next(a))

# Removing Duplicate items from the list
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

for num in compact(sorted(numbers)):
    print(num)


# is_anagram
def is_anagram(word1: str, word2: str) -> bool:
    is_same_words = word1.lower() != word2.lower()
    has_same_letters = sorted(word1.lower()) == sorted(word2.lower())
    return has_same_letters and is_same_words


print(is_anagram('Listen', 'Silent'))   # Prints True
print(is_anagram('tea', 'eat'))     # Prints True
print(is_anagram('Bat', 'Pat'))     # Prints False


# Print earlist date
m, d, y = "01/27/1832".split('/')
d_d1 = datetime.date(int(y), int(m), int(d))
m, d, y = "01/27/1756".split('/')
d_d2 = datetime.date(int(y), int(m), int(d))

if d_d1 > d_d2:
    print('earlist date ', d_d2)
else:
    print('earlist date ', d_d1)

# Most common words
words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
        ]
words_count = collections.Counter(words)
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


print(lstrip(numbers, 0))


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
def uniques_only(iterable, key=None):
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
