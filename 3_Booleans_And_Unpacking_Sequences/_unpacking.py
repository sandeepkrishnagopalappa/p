"""
1. A sequence is an object which can be indexed.
2. Any object which implements __getitem__ is a sequence.
3. All Sequences are Iterables. But all iterables are not sequences.
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
# * is used to grab excess arguments/items
least, *rest, maximum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(least)    # Prints first item in the list
print(maximum)  # Prints last item in the list
print(rest)     # Prints all the item in between 1st and last item of the list
print(max(rest))
print(min(rest))

*trailing, current = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(trailing)
print(current)

a, b, *c = range(1, 10)
a, b, *rest = range(2)

# Ignoring certain values while unpacking
# _ is called throwaway variable in python
data = ['IBM', 50, 91.1, (2019, 7, 17)]
name, *_, (year, *_) = data

# Deep Unpacking
temperatures = {"Bangalore": (26, 32), "Chennai": (29, 35), "Delhi": (31, 36)}

for city, (_min, _max) in temperatures.items():
    print(city, _min, _max)
