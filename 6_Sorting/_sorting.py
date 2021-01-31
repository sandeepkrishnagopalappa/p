# SORTING Iterables

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
sorted_names = sorted(names)    # sorted method returns a new list in sorted order
print('Sorted List', sorted_names)
print('Original List', names)       # Original list remains un-changed

names.sort()    # sort method sorts the original list inplace
print('Sorted List', names)

reverse_names = sorted(names, reverse=True)
print(reverse_names)    # sorts the list in decending order

# ======================================================
# SORTING TUPLES
tup = (1, 2, 5, 3, 9, 8, 6, 7, 0)
# Tuple does not have method .sort() to sort it inplace. So we have to use sorted() method to sort tuple's
sorted_tup = sorted(tup)
print('Sorted Tuple ', sorted_tup)

# Sorting Dictionary
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }

sorted_dict = sorted(prices)

print(sorted_dict)      # Sorts the keys of the dictionary in ascending order

# ==========================================================================
# Custom Sorting
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

# Sorting the list based on the number of characters of the list item
print(sorted(names, key=len))

# Sorting the list based on the last character of the list item
l = ['aw', 'bv', 'cu', 'dt']
s = sorted(l, key=lambda item: item[-1])

# Sorting based on temperatures
def get_temp(item):
    return item[-1]

temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]
sorted(temperatures, key=get_temp)
sorted(temperatures, key=lambda item: item[-1])

# Sorting Dictionary based on values
my_dict = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
print(sorted(my_dict.items(), key=lambda item: item[1]))

# Sorting Dictionary based on share price
prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
        }

s_prices = sorted(prices.items(), key=lambda d: d[-1])
min_p, *_, max_p = sorted(prices.items(), key=lambda d: d[-1])

print(min_p)
print(max_p)

# OR

min_price = min(s_prices, key=lambda item: item[-1])
max_price = max(s_prices, key=lambda item: item[-1])

portfolio = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1},
                {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]

def get_share_name(item):
    return item['name']

def get_no_shares(item):
    return item['shares']

def get_share_price(item):
    return item['price']

# Sorts based on share name
sorted(portfolio, key=get_share_name)
sorted(portfolio, key=lambda d: d.get('name'))

# Sorts based on number of shares
sorted(portfolio, key=get_no_shares)
sorted(portfolio, key=lambda d: d.get('shares'))

# Sorts based on number of price
sorted(portfolio, key=get_share_price)
print(sorted(portfolio, key=lambda d: d.get('price')))

data = [
    {'fname': 'Steve', 'eid': 1003, 'lname': 'Wazniak'},
    {'fname': 'Steve', 'eid': 1002, 'lname': 'Jobs'},
    {'fname': 'Alex', 'eid': 1001, 'lname': 'Martin'},
    {'fname': 'Brain', 'eid': 1004, 'lname': 'Jones'},
]

def get_fname(item):
    return (item['fname'], item['lname'])

s = sorted(data, key=get_fname)
s = sorted(data, key=lambda item: (item['fname'], item['lname']))

# Sorting a Custom Class
class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary


emp1 = Employee('steve', 'jobs', 90000)
emp2 = Employee('bill', 'gates', 80000)
emp3 = Employee('joseph', 'trev', 70000)

li_emp = [emp1, emp2, emp3]

# Sorting Employee objects based on salary
s = sorted(li_emp, key=lambda emp: emp.salary)