import heapq
import string
import math

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

# Returns a list containing all vowels in the given string
my_string = 'Hello world'
person_names = ['Laura', 'Steve', 'Bill', 'James', 'Bob', 'Greig', 'Scott', 'Alex', 'Ive']


# Names starting with Vowels
def get_vowel_names(iterable):
    return [name for name in iterable if name[0].lower() in ['a', 'e', 'i', 'o', 'u']]


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

# Dictionary Comprehension
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
