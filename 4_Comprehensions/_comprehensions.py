import math

'''
Comprehensions in Python is a way to build an iterable object in one expression without the need of traditional
for loop.
'''
# List 4_Comprehensions are used for building a new list
# Square Numbers_And_Booleans in the list. Using 'for' loop
nums = [1, 2, 3, 4, 5]

# Square Numbers in the list. Using List 4_Comprehensions
list_evens = [num ** 2 for num in nums]

# Convert to upper case
sentence = "This is bunch of words"
cap = [word.upper() for word in sentence.split()]

# Returns a list containing all vowels in the given string
names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
vowel_names = [name for name in names if name[0] in "aeiou"]

# Names starting with consonents
names = [name for name in names if not name.startswith(('a', 'e', 'i', 'o', 'u'))]

# Raise to the power of list index
a = [1, 2, 3, 4, 5]
i = [value ** index for index, value in enumerate(a)]

# Build a list of tuples with string and its length pair
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
str_len_pair = [(name, len(name)) for name in names]

# List of even numbers between range 1-50
even_numbers = [num for num in range(1, 50) if num % 2 == 0]

# Build a list with only even with even length string
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
even_string = [name for name in names if len(name) % 2 == 0]

# Generating List of PI values
pi_list = [round(math.pi, n) for n in range(1, 6)]

# Removing Duplicate items from the list
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
numbers = sorted(numbers)
dedup = [number for index, number in enumerate(numbers) if index == 0 or number != numbers[index-1]]

# List comprehension to sum the factorial of numbers from 1-5
a = [1, 2, 3, 4, 5]
s = sum([math.factorial(number) for number in a])

# Using "else" in Comprehension
data = ['hello', 123, 1.2, 'world', True, 'python']
d = [item[::-1] if isinstance(data, str) else item for item in data]

# Reverse the string if the string is of odd length, otherwise keep it as is.
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
_names = [name[::-1] if len(name) % 2 == 0  else name for name in names]


# Dictionary Comprehension
# Building a dict of word and length pair
words = "This is a bunch of words"
d = {word: len(word) for word in words.split()}

# Flipping keys and values of the dictionary using dict comprehension
d = {'a': 1, 'b': 2, 'c': 3}

f = {value: key for key, value in d.items()}

sentence = '''Python is an easy to learn, powerful programming language. 
It has efficient high-level data structures and a simple but effective approach to object-oriented programming.
Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language 
for scripting and rapid application development in many areas on most platforms.'''
dict_word_count = {word: sentence.count(word) for word in sentence.split(' ')}

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

# Buildings
buildings = {
                'burj khalifa':                     828,
                'Shanghai_Tower':                   632,
                'Abraj_Al_Bait_Clock Tower':        601,
                'Ping_An_Finance_Centre_Shenzhen':  599,
                'Lotte World Tower':                554.5,
                'World Trade Center':               541.3
                }

buildings_feets = {building: height * 3.28 for building, height in buildings.items()}


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

# Dial Codes
dial_codes = [
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

country_codes = {code: country for code, country in dial_codes}

# Building a dictionary with type and data mapping
data = [1, 1.2, 'hello', len, True, (1, 2, 3), {9, 8, 6}, ['apple', 'ibm', 'yahoo']]
print({type(item): data for item in data})

# Building a dictionary whose price value is more than 200
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p = {company: price for company, price in prices.items() if price > 200}

# Set Comprehension
# The difference between Dictionaty Comprehension and Set Comprehension is that the set Comprehension does not
# have key value pair

nums = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
s = {num ** 2 for num in nums}
print(s)

# Nested 4_Comprehensions
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
