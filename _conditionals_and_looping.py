_month = 'January'

if _month == 'January':
    print('You are in Jan')
elif _month == 'March':
    print('You are in Mar')
elif _month == 'July':
    print('You are in Jul')
else:
    print('Unknown month')
# =================================================
# Looping
for num in range(5):
    print(num)

for x in range(5):
    print('Python is awesome')

for num in range(0, 10, 2):
    print(num)

months = ['january', 'march', 'may', 'july']
for month in months:
    print(len(month), month)


counter = 0
while counter < 5:
    print('Python is awesome')
    counter += 1

# ===================================================
# Break and Continue statements
my_num = 10
for num in range(100):
    if num == my_num:
        print(num)
        break
    else:
        print(num)

for num in range(51):
    if num % 2 == 0:
        continue
    else:
        print(num)

numbers = [1, 3, 5, 7, 9]
for num in range(10):
    if num in numbers:
        continue
    else:
        print(num)
# ======================================================
