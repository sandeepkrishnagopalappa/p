import heapq
import string
import math
from collections import Counter
from collections import defaultdict

'''
Comprehensions in Python is a way to build an iterable object in one expression without the need of traditional
for loop.
'''
# List Comprehensions are used for building a new list
# Square Numbers_And_Booleans in the list. Using 'for' loop
nums = [1, 2, 3, 4, 5]

# Square Numbers in the list. Using List Comprehensions
list_evens = [num ** 2 for num in nums]
print(list_evens)

# Convert to upper case
sentence = "This is bunch of words"
cap = [word.upper() for word in sentence.split()]

# Returns a list containing all vowels in the given string
my_string = 'Hello world'
person_names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']


# Names starting with Vowels
def get_vowel_names(iterable):
    return [name for name in iterable if name[0].lower() in ['a', 'e', 'i', 'o', 'u']]


# Names starting with consonents
names = [name for name in person_names if not name.startswith(('a', 'e', 'i', 'o', 'u'))]


# Names starting with Vowels
def get_vowel_names2(iterable):
    return [name for name in iterable if name[0].startswith(tuple(['a', 'e', 'i', 'o', 'u']))]


def get_vowel_names3(iterable):
    return [name for name in iterable if name[0] in 'aeiou']


print(get_vowel_names(person_names))
print(get_vowel_names(my_string))


# Raise to the power of list index
def raise_to_index(iterable):
    return [value ** index for index, value in enumerate(iterable)]


nums = [1, 2, 3, 4, 5]
print(raise_to_index(nums))

# List of even numbers between range 1-50
even_numbers = [num for num in range(1, 50) if num % 2 == 0]
print(even_numbers)

# Generating List of PI values
pi_list = [round(math.pi, n) for n in range(1, 6)]
print(pi_list)

# Removing Duplicate items from the list
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
numbers = sorted(numbers)
dedup = [number for index, number in enumerate(numbers) if index == 0 or number != numbers[index-1]]
print(dedup)

# List comprehension to sum the factorial of numbers from 1-5
a = [1, 2, 3, 4, 5]


def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)


s = sum([fact(number) for number in a])

# Prints the names if the first char of the item starts with any letter in the first half of the alphabet character
names = ['apple', 'yahoo', 'google', 'facebook', 'dropbox', 'instagram', 'twitter', 'microsoft', 'next']
first_half_alphabets = string.ascii_lowercase[:13]
first_half = [name.title() for name in names if name[0] in first_half_alphabets]
print(first_half)


# Reverse firstname and lastname in the list using list comprehension
def reverse_names(name):
        fname, lname = name.split()
        return f'{lname.title()} {fname.title()}'


fullnames = ['steve jobs', 'bill gates', 'tim cook', 'johny ive']
rev_fname_lname = [reverse_names(name) for name in fullnames]
print(rev_fname_lname)

# Reverse difference
nums = [1, 2, 3, 4, 5]
reverse_difference = [n1 - n2 for n1, n2 in zip(nums, nums[::-1])]
print(reverse_difference)

# Deleting Sequence
sequence = [1, 2, 1, 1, 1, 2, 3, 4, 2, 2]
seq = [item for index, item in enumerate(sequence) if index == 0 or item != sequence[index - 1]]
print(seq)  # Prints [1, 2, 1, 2, 3, 4, 2]

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

# Getting user names from password.txt
l = [line.split(":")[0] .strip() for line in open('linux-etc-passwd.txt') if not line.strip().startswith("#")]

# Getting only ip addresses from web server log. Also, find out how may times
# Each IP address is appears in the list and create a dictionary.
ip = [line.split()[0] for line in open("access-log.txt")]

# Using Normal Dict
dd = {}

for item in ip:
    if item in dd:
        dd[item] += 1
    else:
        dd[item] = 1
print(dd)

# using Default Dict
d = defaultdict(int)
for item in ip:
    d[item] += 1
print(d)

# Using Counter object
c = Counter()
for item in ip:
    c[item] += 1

print(c)

# Dictionary Comprehension
# Building a dict of word and length pair
words = "This is a bunch of words"
d = {word: len(word) for word in words.split()}

# Flipping keys and values of the dictionary using dict comprehension
d = {'a': 1, 'b': 2, 'c': 3}

f = {value: key for key, value in d.items()}

# Searching for a word in the file
s = {word.strip() for word in open("words")}
sentence = "Hello there. this is bunch of words Aaronical and resnub"
w = {word: word in s for word in sentence.split()}

sentence = '''Python is an easy to learn, powerful programming language. 
It has efficient high-level data structures and a simple but effective approach to object-oriented programming.
Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language 
for scripting and rapid application development in many areas on most platforms.'''
dict_word_count = {
    word: sentence.count(word)
    for word in sentence.split(' ')
}
print(dict_word_count)

# Counting the number of each character in a String
my_string = 'guido van rossum'
dict_char_count = {c: my_string.count(c) for c in my_string}
print(dict_char_count)

# Dictionary of character and ascii value pairs
s = 'abcABC'
dict_ascii = {
    c: ord(c)
    for c in s
}
print(dict_ascii)

# Tallest Buildings
tall_buildings = {
                'burj khalifa':                     828,
                'Shanghai_Tower':                   632,
                'Abraj_Al_Bait_Clock Tower':        601,
                'Ping_An_Finance_Centre_Shenzhen':  599,
                'Lotte World Tower':                554.5,
                'World Trade Center':               541.3
                }


def to_feets(m):
    return round(m * 3.28)


tall_buildings_feets = {
                        building: to_feets(height)
                        for building, height in tall_buildings.items()
                    }
print(tall_buildings_feets)

# Creating Dictionary of city and population pairs using Dict Comprehension
cities = ['Tokyo',
          'Delhi',
          'Shanghai',
          'Sao Paulo',
          'Mumbai'
          ]

population = ['38,001,000',
              '25,703,168',
              '23,740,778',
              '21,066,245',
              '21,042,538'
              ]

pairs = {city: population for city, population in zip(cities, population)}

print(pairs)

# Dial Codes
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
    ]

country_codes = {code: country for code, country in DIAL_CODES}

# Building a dictionary with type and data mapping
data = [1, 1.2, 'hello', len, True, (1, 2, 3), {9, 8, 6}, ['apple', 'ibm', 'yahoo']]
print({type(item): data for item in data})

# Type Conversion of Data
data = ['IBM', '100', '91.2']
types = [str, int, float]

converted = [func(item) for func, item in zip(types, data)]

# Building a dictionary whose price value is more than 200
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p = {company: price for company, price in prices.items() if price > 200}

# Removing duplicates from the list (using Dictionary and List Comprehension)
l = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
d = {item: l.count(item) for item in l}
[l.remove(key) for key, value in d.items() if value > 1]
print(l)

# Counts the occurance of each word in the text file and prints the most and least repeated words
with open('read.txt', 'r') as f:
    text = f.read()
    d = {
        word: text.count(word)
        for word in text.split(' ')
    }

print('Original dictionary --->', d)

print(heapq.nlargest(3, d.items(), key=lambda name: name[-1]))

print(heapq.nsmallest(3, d.items(), key=lambda name: name[-1]))

# Unpacking List the rest of the words between least and maximum
least, *rest, maximum = sorted(d.items(), key=lambda name: name[-1])
print(least)    # Prints the word with least occurance
print(maximum)  # Prints the word with maximum occurance
print(rest)     # Prints all elements between 1st and last element

# Set Comprehension
# The difference between Dictionaty Comprehension and Set Comprehension is that the set Comprehension does not
# have key value pair

nums = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
s = {num ** 2 for num in nums}
print(s)

# Getting Unique IP's from the web server log.
ip = {line.split(':')[0] for line in open('access-log.txt')}

# Getting Unique shell from the password.txt file
l = {line.split(":")[-1].rstrip()
     for line in open('linux-etc-passwd.txt')
     if line.strip() and not line.startswith("#")
     }

for item in l:
    print(item)

# Nested Comprehensions
n = [(x, y) for x in range(5) for y in range(5)]

countries = {"India": ["Bangalore", "Chennai", "Delhi", "Kolkata"],
             "USA": ["Dallas", "New York", "Chicago"],
             "China": ["Bejing", "Shaingai"]
             }

# Get the list of Country and City in a tuple
# [("India", "Bangalore"),("India", "Chennai"),("India", "Delhi"),
# ("India", "Kolkata"),("USA", "Dallas"), ("USA", "New York"),
# ("USA", "Chicago"), ("China", "Bejing"), ("China", "Shaingai")]

l = [(country, city) for country, cities in countries.items() for city in cities]


# list of Dicts from shoe data
def make_dict(line):
    data = line.strip().split('\t')
    return {"brand": data[0], "color": data[1], "size": data[2]}


s = [make_dict(line) for line in open('shoe-data.txt')]

for item in s:
    print(item)


