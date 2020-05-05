import heapq
from operator import itemgetter, attrgetter

# Custom Sorting
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

# Sorting the list based on the number of characters of the list item
print(sorted(names, key=len))

# Sorting the list based on the last character of the list item
print(sorted(names, key=lambda name: name[-1]))

portfolio = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1},
                {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]
  
print(sorted(portfolio, key=lambda d: d.get('name')))   # Sorts on the key 'name'
print(sorted(portfolio, key=lambda d: d.get('shares')))   # Sorts on the key 'shares'
print(sorted(portfolio, key=lambda d: d.get('price')))   # Sorts on the key 'price'

# Sorting using itemgetter
print(sorted(portfolio, key=itemgetter('name')))

print(sorted(portfolio, key=itemgetter('name', 'shares')))

data = [
    {'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'},
    {'fname': 'David', 'uid': 1002, 'lname': 'Beazley'},
    {'fname': 'John', 'uid': 1001, 'lname': 'Cleese'},
    {'fname': 'Big', 'uid': 1004, 'lname': 'Jones'},
]

print(sorted(data, key=itemgetter('fname', 'lname')))
print(sorted(data, key=itemgetter('lname', 'fname')))


# Sorting Employee Class
class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def __repr__(self):
        return f'({self.fname}, {self.lname}, {self.salary})'

    def full_name(self):
        return self.fname + ' '+self.lname

    def email(self):
        return f'{self.fname}.{self.lname}@company.com'


emp1 = Employee('steve', 'jobs', 90000)
emp2 = Employee('bill', 'gates', 80000)
emp3 = Employee('joseph', 'trev', 70000)

li_emp = [emp1, emp2, emp3]

print(sorted(li_emp, key=lambda emp: emp.salary))


# or Implement __lt__ or __gt__ methods in the class
class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def __repr__(self):
        return f'({self.fname}, {self.lname}, {self.salary})'

    def full_name(self):
        return self.fname + ' '+self.lname

    def email(self):
        return f'{self.fname}.{self.lname}@company.com'


emp1 = Employee('steve', 'jobs', 90000)
emp2 = Employee('bill', 'gates', 80000)
emp3 = Employee('joseph', 'trev', 70000)

li_emp = [emp1, emp2, emp3]

print(sorted(li_emp))
# Prints
# [(joseph, trev, 70000), (bill, gates, 80000), (steve, jobs, 90000)]

print(heapq.nlargest(2, [(emp.salary, emp.full_name()) for emp in li_emp]))
print(heapq.nsmallest(2, [(emp.salary, emp.full_name()) for emp in li_emp]))

# Sorting using attgetter
print(sorted(li_emp, key=attrgetter('salary')))

# Merging and sorting two different lists
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

c = heapq.merge(a, b)

for item in c:
    print(item)
