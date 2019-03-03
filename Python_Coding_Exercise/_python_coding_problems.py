from itertools import groupby
import datetime
import collections

# Coding Problem-1
lst1 = [42, 3, 9, 42, 42, 0, 9, 42, 42, 17, 8, 222, 4, 9, 0, 1]
lst2 = [42, 222, 9]
for item in reversed(lst1):
    if item in lst2:
        lst1.remove(item)
        lst1.append(0)
print(lst1)     # [3, 0, 17, 8, 4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Coding Problem-2
l1 = [1, 2, 3, 4, 5, 6]
l2 = [l1[item] for item in range(1, len(l1), 2)]
l3 = [l1[item] for item in range(0, len(l1), 2)]
result = [a + b for a, b in zip(l2, l3)]
print(result)

# Coding Problem-3 Print total duplicates in the list
nums = [1, 2, 3, 1, 3, 5, 4, 3, 3, 1, 1, 1, 1]
duplicates = 0
for num in nums:
    if nums.count(num) > 1:
        duplicates += 1
print('Number of Duplicates ', duplicates)

# Febinocci Series
f_num = 5
counter = 0
a = 0
b = 1
while counter < f_num:
    print(a, end=',')
    a, b = a + b, a
    counter += 1
    
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
