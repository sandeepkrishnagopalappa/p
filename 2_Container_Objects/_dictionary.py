from collections import OrderedDict
from collections import defaultdict
# PYTHON DICTIONARIES

# Different ways of constructing a dictionary
d = {}
d = dict()
d = dict(Bangalore=25, Chennai=35, Delhi=30)
d = dict([("Bangalore", 25), ("Chennai", 35), ("Delhi", 30)])
d = dict(zip(["Bangalore", "Chennai", "Delhi"], [25, 35, 30]))
d = dict({'Bangalore': 25, "Chennai": 35, "Delhi": 30})

print(len(d))    # Prints the length of the dictionary

# Accessing elements of a dictionary
print(d['Bangalore'])
print(d.get('Bangalore'))

location = {'country': 'India', 'states': ['Karnataka', 'Anrda', 'Kerala']}

# Nested Dictionary
prices = {'IBM': {'current': 90.1, 'low': 88.3, 'high': 92.7}}
print(prices['IBM']['current'])
print(prices['IBM']['high'])

# Accessing a key that does not exist
# print(employee['age'])      # Throws exception KeyError: 'age'
print(d.get('Noida'))      # get() method Does not throw an exception, but returns 'None'
print(d.get('Noida', 'The Key not found in the dictionary'))   # Throws exception KeyError: 'age'

# Adding / Updating the dictionary
d.update({"Mysore": 26, "Cochin": 28})
d['Mysore'] = 26.5  # Upadting the dictionary key with new value

# Deleting the key and value
d.popitem()      # Returns and deletes the last key/value pair in the dictionary
print(d.pop('age'))    # Returns and Deletes the mentioned key from the dictionary
# del employee['age']     # Deletes the Key 'age' and its value

# Looping through Key's and Value's of the Dictionary
print(d.items())     # Returns a tuple of key,value pairs

for item in d:      # Prints only key's of the dictionary
    print(item)
    
for item in d:
    print(d[item])   # Prints Values of the dictionary

for key, value in d.items():     # Tuple un-packing
    print(key, value)

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for index, items in enumerate(d.items()):
    print(index, items)

# Merging Dictionaries
d1 = {'fname': 'steve', 'lname': 'jobs'}
d2 = {'age': 56, 'company': 'apple'}

d3 = {**d1, **d2}

# Creating Dictionary using List's
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

dict_city_pairs = dict(zip(cities, population))

print(dict_city_pairs)    # Prints dictionary of city and population pairs
# {'Tokyo': '38,001,000', 'Delhi': '25,703,168', 'Shanghai': '23,740,778',
# 'Sao Paulo': '21,066,245', 'Mumbai': '21,042,538'}

# Count number of words in a sentence
sentence = 'hello world hello world welcome to python'
words = sentence.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

# defaultDict
word_count = defaultdict(int)

for word in words:
    word_count[word] += 1

profile = defaultdict(list)     # One to Many Mapping
profile['language'].append('Java')
profile['language'].append('Python')


cities = [('India', 'Bangalore'),
          ('India', 'Chennai'),
          ('India', 'Delhi'),
          ('India', 'Kolkata'),
          ('USA', 'Dallas'),
          ('USA', 'New York'),
          ('USA', 'Chicago'),
          ('China', 'Bejing'),
          ('China', 'Shaingai')
          ]

dd = defaultdict(list)
for country, city in cities:
    dd[country].append(city)

# Composite Keys
# Dictionary key must be of Immutable Type. e.g
# Dict keys should always be Hashable. (All immutable objects are Hashable)
holidays = {
    (26, 1): 'Republic Day',
    (15, 8): 'Independance Day',
    (25, 6): 'Yoga Day'
}

# OrderedDict
# Ordered Dictonary Maintains Order
d = OrderedDict()
d['apple'] = 'A'
d['google'] = 'G'
d['yahoo'] = 'Y'

for key, value in d.items():
    print(key, value)
