# PYTHON DICTIONARIES

# Creating an empty Dictionary
employee = {}
employee = dict()   # Using Constructor

# Adding elements to an empty dictionary
employee['name'] = 'steve'
employee['salary'] = 60000

print(employee)

employee = {'name': 'steve', 'salary': 60000, 'languages': ['java', 'python']}

print(len(employee))    # Prints the length of the dictionary

# Accessing elements of a dictionary
print(employee['name'])
print(employee['languages'])
print(employee.get('salary'))

# Accessing a key that does not exist
# print(employee['age'])      # Throws exception KeyError: 'age'
print(employee.get('age'))      # get() method Does not throw an exception, but returns 'None'
print(employee.get('age', 'The Key not found in the dictionary'))   # Throws exception KeyError: 'age'

# Adding / Updating the dictionary
employee.update({'age': 35, 'phone': '111-1111'})
employee = {**employee, 'address': '2200, Valley View Lane'}

# Deleting the key and value
employee.popitem()      # Returns and deletes the last key/value pair in the dictionary
print(employee.pop('age'))    # Returns and Deletes the mentioned key from the dictionary
# del employee['age']     # Deletes the Key 'age' and its value

# Looping through Key's and Value's of the Dictionary
employee = {'name': 'steve', 'salary': 60000, 'languages': ['java', 'python']}

print(employee.items())     # Returns a tuple of key,value pairs

for item in employee:      # Prints only key's of the dictionary
    print(item)
    
for item in employee:
    print(employee[item])   # Prints Values of the dictionary

for key, value in employee.items():     # Tuple un-packing
    print(key, value)

for key in employee.keys():
    print(key)

for value in employee.values():
    print(value)

for index, items in enumerate(employee.items()):
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

pairs = dict(zip(cities, population))

print(pairs)    # Prints dictionary of city and population pairs

# Prints default value zero if the key is not found in the dictionary
print(pairs.get('Bangalore', 0))

# Count number of words in a sentence
sentence = '''
Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability,
notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.
Van Rossum led the language community until stepping down as leader in July 2018.
'''
words = sentence.split()

words_count = {}

for word in words:
    word_count = words.count(word)
    words_count.update({word: word_count})

print(words_count)