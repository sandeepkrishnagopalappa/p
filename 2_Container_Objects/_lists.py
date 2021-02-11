from itertools import zip_longest

# PYTHON LISTS
"""
1. Lists are Mutable
2. Elements in the Lists are Ordered
3. Lists can hold duplicate elements
4. Lists can be indexed by integers starting zero
"""

# Creating an empty List
my_list = []
my_list = [1, 2, 3, 4, 5]
my_list = list()    # Using list constructor
my_list = list('helloworld')
my_list = list([1, 2, 3, 4, 5])

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

print(names)    # Prints the items of the List
print(len(names))       # Prints the Length of the List. Index starts from Zero.
print(names[0])     # Prints the item present in the 0th index of the List.


# Adding elements to the List
names.append('gmail')   # Adding element to the list
names.insert(3, 'watsapp')      # Inserts the item at 3rd index.
names.extend(['netflix', 'walmart', 'kroger'])    # Adds the new list to the existing list
names = [*names, 'signal']  # Adds the new list to the existing list
print(names)

print('gmail' in names)     # Prints True if the item is present in the list

# Removing Items from the List
names.remove('kroger')  # Removes the item 'kroger' from the List
names.pop()     # By default this will remove the last item in the List
# pop method returns the item that it has removed from the List
names.pop(3)    # Removes the item in the 3rd index of the List

del names[0]    # Deletes 0th item in the list
# del names[3:6]  # Deletes 3rd, 4th and 5th items in the list
# del names[::2]  # Deletes alternate items in the list
# del names   # Deletes the reference to the list "names"
# del names       # Deletes the entire list

# Making copy of the list (Shallow Copy!!!)
a = [1, 2, 3, 4, 5]
b = a.copy()
  # OR
b = a[:]

# 6_Sorting List's
names.sort()    # Sorts the List in Alphabetical Order
# sort method modifies the list inplace.
names.sort(reverse=True)    # Sorts the List in Decending Order

sorted(names)   # Sorts the List in Alphabetical Order and returns a new list.
# sorted method does not alter the existing list.

sorted(names, reverse=True)     # Sorts the List in Decending Order

names.index('google')       # Returns the index of the item in the List

print('yahoo' in names)    # Returns True if the item present in the List

# Iterating through the List
for item in names:
    print(item)

# Iterating over a part of the list
for item in names[:4]:
    print(item)

# Prints the item and its corresponding index in the list
for index, item in enumerate(names):    # enumerate returns a tuple of index, item pair
    print(index, item)

for index, item in enumerate(names, start=1):   # Index starts from 1
    print(index, item)

# ================================================================================
# Iterating over multiple lists simultaniously
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai']
population = ['38,001,000', '25,703,168', '23,740,778', '21,066,245', '21,042,538']

# Iterating through multiple list Non-Pythonic approach
for i in range(len(cities)):
    print(cities[i], population[i])

# Iterating through multiple list using zip function
for city, population in zip(cities, population):
    print(city, population)

# Iterating through multiple list with un-equal lengths using zip function
a = [1, 2, 3]
b = ['v', 'w', 'x', 'y', 'z']

for i in zip(a, b):
    print(i)    # Prints (1, 'v'), (2, 'w'), (3, 'x')
    # zip function stops at the shortest list

for i in zip_longest(a, b):
    print(i)    # Prints (1, 'v'), (2, 'w'), (3, 'x'), (None, y), (None, z)

for i in zip_longest(a, b, fillvalue='NA'):
    print(i)    # Prints (1, 'v'), (2, 'w'), (3, 'x'), ('NA', y), ('NA', z)

a = [1, 2, 3]
b = ['x', 'y', 'z']
c = ['alpha', 'beta', 'gamma']

for i in zip(a, b, c):
    print(i)    # Prints (1, 'x', 'alpha'), (2, 'y', 'beta'), (3, 'y', 'gamma')
# ================================================================================

files = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.pdf', 'apple.doc']
for file in files:
    if file.endswith('pdf'):
        print(file)

# ===========OR==========
for file in files:
    if file[-3:] == 'pdf':
        print(file)

filenames = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.py', 'apple.doc']
# Multiple conditions in startswith and endswith function
for filename in filenames:
    if filename.endswith(('txt', 'pdf')):   # filename either endswith txt or pdf
        # startswith and endswith can take tuple as an argument
        print(filename)

# Converting Lists to String
print('-'.join(names))  # Prints yahoo-netflix-microsoft-instagram-google-gmail-facebook-apple-amazon
print('|'.join(names))  # Prints yahoo|netflix|microsoft|instagram|google|gmail|facebook|apple|amazon
print(','.join(names))  # Prints yahoo,netflix,microsoft,instagram,google,gmail,facebook,apple,amazon
