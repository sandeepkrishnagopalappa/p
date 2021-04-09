# range(start, end, step)
# Start index is always included.
# End index is always excluded.

# Prints numbers from 0 to 4 (upto 5 but not including 5)
for num in range(0, 5):
    print(num)  # prints 0, 1, 2, 3, 4

# Prints numbers from 0 to 4 (num starts from zero if start index is omitted)
for num in range(5):
    print(num)  # Prints 0, 1, 2, 3, 4

# Prints every altrante numbers starting zero
for num in range(0, 10, 2):
    print(num)      # Prints 0, 2, 4, 6, 8

# Prints number from 10 to 1
# In the below example end index is zero. So python prints numbers from
# 10 to 1. End index excluded.
for num in range(10, 0, -1):
    print(num)      # Prints 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# Prints number form 10 to 0
for num in range(10, -1, -1):
    print(num)      # Prints 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0

# Prints alternate numbers from 10 to 0.
for num in range(10, -1, -2):
    print(num)      # Prints 10, 8, 6, 4, 2, 0

# Prints "Python is awesome!!" 5 times
for i in range(5):
    print('Python is awesome!!')

for _ in range(5):
    print('Python is awesome!!')
# Since we are not making use of any loop variable inside for loop, we
# can simply give _ (underscore). _ is called throw away variable in Python.
