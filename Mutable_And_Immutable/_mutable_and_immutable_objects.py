# Strings are Immutable Objects
name = 'hello'
name[0] = 'y'   # Assignment not possible

nums = [1, 2, 3, 4, 5]
nums[0] = 100   # Assignment possible

my_tuple = (1, 2, ['a', 'b', 'c'], 3)
my_tuple[0] = 10    # Assignment not possible
my_tuple[2][0] = 'x'    # Assignemnt possible

name = 'a'
print(name)
print(f'Memory Address of {name} is {id(name)}')

name = 'b'      # A new String gets returned when the name variable is re-assigned with value 'b'
print(name)
print(f'Memory Address of {name} is {id(name)}')

other_name = name

name = 'c'
print(name)
print(other_name)   # other_name still holds the value 'b' even though name variable is changed to 'c'
# ====================================================

# Lists are Mutable Objects
names = ['apple', 'yahoo', 'google']
print(names)
print(f'Memory Address of {names} is {id(names)}')

other_names = names     # Both names and other_names are pointing to the same memory location or Object
print(f'Memory Address of {other_names} is {id(other_names)}')

names[0] = 'instagram'  # Modify the original List 'names'
print(other_names)      # 'other_names' will also get the modified copy of 'names'
# ====================================================

# Example:

employees = ['steve', 'mark', 'rick', 'bill', 'laura']

output = []     # Let's declare the variable 'output' as List object

for employee in employees:
    output.append(employee)
    print(id(output))
print(output)

# The output of the above code is
# 6539544
# 6539544
# 6539544
# 6539544
# 6539544
# ['steve', 'mark', 'rick', 'bill', 'laura']

output = ''     # Let's declare the variable 'output' as String object

for employee in employees:
    output = employee+','+output
    print(id(output))
print(output)

# The output of the above code is
# 15621984
# 13312632
# 15570608
# 15570512
# 13147736
# laura,bill,rick,mark,steve,

# The Usage of Memory is more in case of Strings and less in case of List
