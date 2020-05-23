# Sets are Python's builtin data type which has the following characterstics
#    1. Sets are unordered
#    2. Elements inside the sets are unique
#    3. Sets are mutable, but elements inside the set must be hasable
#    4. Sets cannot be indexed or sliced

# Hashable Objects:
# Hashable objects are the objects which implements __hash__ magic method and
# hash() method can be called.

# All Immutable objects are hashable, but all hashable objects are not immutable

# Python Sets can only include hashable objects

# Operations on Set
a = {1, 2, 3, 3, 4}
print(len(a))   # Prints the Length of the Set

# Membership test
1 in a  # Prints True if the item is in a

# Set Union
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.union(b)  # Prints {1, 2, 3, 4, 5, 6}

c = {6, 7, 8, 9}

a.union(b, c)   # Prints {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Set Intersection
a.intersection(b)   # Prints {3, 4}

# Set Difference
# Prints all the elements in set a which are not in b
a.difference(b)
# a - b   # Prints {1, 2}

a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}
a.difference(b, c)  # Prints {1, 2, 3}
# a - b - c
