# SLICING PYTHON LIST's

# Slicing List's
# names[start:stop:step]
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
#       [   0         1         2       3           4           5           6      ]
#       [  -7        -6        -5      -4          -3          -2          -1      ]
print(names[2:5])   # Prints all the items from 2nd index upto but not including 5th index.
print(names[:4])    # Prints all items from 0th index and upto 4th index, but not including 4th index.
print(names[2:])    # Prints all items from 2nd index till the end of the List.

# Expression inside square brackets
print(names[1 + 3])  # Prints 4th item of the list
print(names[1 - 3])  # Prints 5th item of the list

# Slicing using negative indexing
print(names[-1])    # Prints the last index item of the list
print(names[-7])    # Prints the 0th index item of the list
print(names[-4:-2])     # Prints ['amazon', 'facebook']
print(names[-6:5])      # prints ['google', 'yahoo', 'amazon', 'facebook', 'instagram']
print(names[1:-1])      # prints ['google', 'yahoo', 'amazon', 'facebook', 'instagram']
print(names[:-1])   # Prints ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram']

print(names[:])     # Prints the entire list
print(names[::2])   # Prints alternate items in the list
print(names[::-1])  # Prints the items in the list in reverse order

print(names[::2])   # Prints alternate items in the list
print(names[2:7:2])
print(names[-1:2:-1])
print(names[::-1])      # Prints the list in Reverse order

names[:2] = ['unknown', 'Unknown']  # Replacing Multiple items in the list
print(names)

# Print the extension of each file name in the list
files = ['youtube.txt', 'yahoo.pdf', 'microsoft.doc', 'apple.xls', 'amazon.xml']
for file in files:
    print(file[-3:])

# Inserting new elements to the list
nums = [1, 2, 3, 4]
nums = nums[:2] + [99, 98, 97] + nums[2:]
print(nums)
# =========================================================================================
