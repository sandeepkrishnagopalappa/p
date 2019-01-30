# SORTING LIST's
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
sorted_names = sorted(names)    # sorted method returns a new list in sorted order
print('Sorted List', sorted_names)
print('Original List', names)       # Original list remains un-changed

names.sort()    # sort method sorts the original list inplace
print('Sorted List', names)

reverse_names = sorted(names, reverse=True)
print(reverse_names)    # sorts the list in decending order

# ======================================================
# SORTING TUPLES
tup = (1, 2, 5, 3, 9, 8, 6, 7, 0)
# Tuple does not have method .sort() to sort it inplace. So we have to use sorted() method to sort tuple's
sorted_tup = sorted(tup)
print('Sorted Tuple ', sorted_tup)

# Sorting Dictionary

profile = {'fname': 'mark', 'lname': 'rob', 'language': ['java', 'python'], 'salary': 90000, 'age': 30}

sorted_dict = sorted(profile)

print(sorted_dict)      # Sorts the keys of the dictionary in ascending order

my_dict = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print(sorted(my_dict.items(), key=lambda item: item[1]))  # Sorts the values of the dictionary in ascending order
