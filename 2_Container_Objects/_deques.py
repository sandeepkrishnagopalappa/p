from collections import deque

""" list-like container with fast appends and pops on either end """

# Make a new deque object with a string
d = deque("hello")  # deque(['h', 'e', 'l', 'l', 'o'])

# add a new entry to the right side
d.append('w')   # deque(['h', 'e', 'l', 'l', 'o', 'w'])

# add a new entry to the left side
d.appendleft('P')   # deque(['P', 'h', 'e', 'l', 'l', 'o', 'w'])

# return and remove the rightmost item
d.pop()     # deque(['P', 'h', 'e', 'l', 'l', 'o'])

# return and remove the leftmost item
d.popleft()     # deque(['h', 'e', 'l', 'l', 'o'])


# To Be Continued....


