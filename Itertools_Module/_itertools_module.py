import itertools

# COUNT
counter = itertools.count()

for _ in range(10):
    print(next(counter))    # Prints numbers from 0 through 9

my_counter = itertools.count(start=5, step=5)   # It can take negative value for step argument

for _ in range(10):
    print(next(my_counter))

names = ['apple', 'microsoft', 'google', 'yahoo']

name_id = zip(itertools.count(), names)

for item in name_id:
    print(item)

# ================================================================
# CYCLE
states = ['ON', 'OFF']

cc = itertools.cycle(states)

for _ in range(5):
    print(next(cc))

# ================================================================
# REPEAT
counter = itertools.repeat(2)

for _ in range(5):  # Repeats the number 5 times
    print(next(counter))

counter = itertools.repeat(2, times=5)

for item in counter:
    print(item)

# ================================================================
# COMBINATION
letters = ['a', 'b', 'c']

my_comb = itertools.combinations(letters, 2)

for item in my_comb:
    print(item)


# ================================================================
# PERMUTATION
my_permutation = itertools.permutations(letters)
# The above code Prints
# ('a', 'b', 'c')
# ('a', 'c', 'b')
# ('b', 'a', 'c')
# ('b', 'c', 'a')
# ('c', 'a', 'b')
# ('c', 'b', 'a')

my_permutation = itertools.permutations(letters, 2)

# The above code prints
# ('a', 'b')
# ('a', 'c')
# ('b', 'a')
# ('b', 'c')
# ('c', 'a')
# ('c', 'b')

for item in my_permutation:
    print(item)

# iSlice

names = ['apple', 'google', 'yahoo', 'flikpart', 'netflix', 'gmail']

my_slice = itertools.islice(names, 2, 5)

for item in my_slice:
    print(item)


# Reading first 5 lines of the file
with open('read.txt') as f:
    lines = f.readlines()
    from itertools import islice
    first_five_lines = islice(lines, 5)
    for line in first_five_lines:
        print(line, end='')
# ================================================================
