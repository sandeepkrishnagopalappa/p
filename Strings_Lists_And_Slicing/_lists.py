# PYTHON LISTS

# Creating an empty List
my_list = []
my_list = list()    # Using list constructor

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

print(names)    # Prints the items of the List
print(len(names))       # Prints the Length of the List. Index starts from Zero.
print(names[0])     # Prints the item present in the 0th index of the List.


# Adding elements to the List
names.append('gmail')   # Adding element to the list
names.insert(3, 'watsapp')      # Inserts the item at 3rd index.
names.extend(['netflix', 'walmart', 'kroger'])    # Adds the new list to the existing list
names = [*names, 'dxc']  # Adds the new list to the existing list
print(names)

print('gmail' in names)     # Prints True if the item is present in the list

# Removing Items from the List
names.remove('kroger')  # Removes the item 'kroger' from the List
names.pop()     # By default this will remove the last item in the List
# pop method returns the item that it has removed from the List
names.pop(3)    # Removes the item in the 3rd index of the List

del names[0]    # Deletes 0th item in the list
# del names       # Deletes the entire list

# Making copy of the list
a = [1, 2, 3, 4, 5]
b = a.copy()
  # OR
b = a[:]
print(a)

# Sorting List's
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

for item in names[:4]:
    print(item)

# Prints the item and its corresponding index in the list
for index, item in enumerate(names):    # enumerate returns a tuple of index, item pair
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
# ================================================================================

files = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.pdf', 'apple.doc']
for file in files:
    if file.endswith('pdf'):
        print(file)

filenames = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.py', 'apple.doc']
for filename in filenames:
    if not filename.endswith('.py'):
        continue
    else:
        print('Python is present!!!!')

# Multiple conditions in startswith and endswith function
for filename in filenames:
    if filename.endswith(('txt', 'pdf')):   # filename either endswith txt or pdf
        # startswith and endswith can take tuple as an argument
        print(filename)

choices = ['http', 'https']
url = 'http://www.python.org'
print(url.startswith(tuple(choices)))


# Converting Lists to String
print('-'.join(names))  # Prints yahoo-netflix-microsoft-instagram-google-gmail-facebook-apple-amazon
print('|'.join(names))  # Prints yahoo|netflix|microsoft|instagram|google|gmail|facebook|apple|amazon
print(','.join(names))  # Prints yahoo,netflix,microsoft,instagram,google,gmail,facebook,apple,amazon

# Converting String to List
my_string = 'Hello World'
print(list(my_string))  # Prints ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
