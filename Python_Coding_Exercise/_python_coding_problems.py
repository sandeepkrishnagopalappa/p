
# Coding Problem-1
lst1 = [42, 3, 9, 42, 42, 0, 9, 42, 42, 17, 8, 222, 4, 9, 0, 1]
lst2 = [42, 222, 9]
for item in reversed(lst1):
    if item in lst2:
        lst1.remove(item)
        lst1.append(0)
print(lst1)     # [3, 0, 17, 8, 4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Coding Problem-2
l1 = [1, 2, 3, 4, 5, 6]
l2 = [l1[item] for item in range(1, len(l1), 2)]
l3 = [l1[item] for item in range(0, len(l1), 2)]
result = [a + b for a, b in zip(l2, l3)]
print(result)

# Coding Problem-3 Print total duplicates in the list
nums = [1, 2, 3, 1, 3, 5, 4, 3, 3, 1, 1, 1, 1]
duplicates = 0
for num in nums:
    if nums.count(num) > 1:
        duplicates += 1
print('Number of Duplicates ', duplicates)

# Febinocci Series
f_num = 5
counter = 0
a = 0
b = 1
while counter < f_num:
    print(a, end=',')
    a, b = a + b, a
    counter += 1
