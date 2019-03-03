"""
A sequence is the one which can be indexed.
Sequences are very common type of iterables in Python.
String's, List's and Tuple's are sequences in python.
Dictionaries, sets are iterables but not Sequences.
All Sequences are Iterables. But all iterables are not sequences
"""

point = (4, 5)  # Unpacking Tuple
x, y = point
print(x)
print(y)

data = ['IBM', 50, 91.1, (2019, 7, 17)]
name, shares, price, date = data    # Unpacking list of items
print(name)
print(shares)
print(price)
print(date)

y, m, d = date  # Unpacking Date

print(y)
print(m)
print(d)

s = 'Hello'
a, b, c, d, e = s   # Unpacking String
print(a)
print(b)
print(c)
print(d)
print(e)

# Unpacking Elements from iterables of Arbitary length
least, *rest, maximum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(least)    # Prints first item in the list
print(maximum)  # Prints last item in the list
print(rest)     # Prints all the item in between 1st and last item of the list
print(max(rest))
print(min(rest))

*trailing, current = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(trailing)
print(current)


# Unpacking list
def add(items):
    head, *tail = items
    if any(tail):
        return head + sum(tail)
    else:
        return head


print(add([1]))
print(add([1, 2, 3, 4, 5]))
