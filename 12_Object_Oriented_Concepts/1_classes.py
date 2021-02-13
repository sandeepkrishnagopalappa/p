import csv

# A class is collection/set of functions that carry out various operations on
# "Instances"

# Instances are the actual objects/data that your function manipulate on.
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def move(self, dx, dy):
        self.a += dx
        self.b += dy

point1 = Point(1, 2)
point2 = Point(10, 20)

print(point1.__dict__)  # {"a": 1, "b": 2}
print(point2.__dict__)  # {"a": 10, "b": 20}

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def attack(self, pts):
        self.health -= pts

p1 = Player(1, 2)
p2 = Player(3, 4)
p3 = Player(5, 6)

# Internally all the instance attributes are stored in a Instance Dictionary.
# All the methods in the class are stored in Class Dictionary

print(p1.__dict__)
print(p1.__class__.__dict__)
print(Player.__dict__)

# Employee Class
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def email(self):
        return f'{self.fname}.{self.lname}@company.com'


e1 = Employee("Steve", "Jobs", 1000)
e2 = Employee("Bill", "Gates", 2000)


class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        self.amount -= amount

    def balance(self):
        print(self.amount)

b1 = BankAccount("steve", 1000)
b2 = BankAccount("bill", 2000)

# Company Class.
class Company:
    def __init__(self):
        self._team = []

    def add_emp(self, name, gender, team, pay):
        self._team.append((name, gender, team, pay))

    # Total Cost
    def total_cost(self):
        total = 0.00
        for emp in self._team:
            total += float(emp[3])
        return total

    # Total Number of male and female employees
    def emp_count_by_gender(self):
        from collections import defaultdict
        _count = defaultdict(int)
        for emp in self._team:
            _count[emp[1]] += 1
        return _count

    # Count of Employees in each department
    def emp_count_by_department(self):
        from collections import defaultdict
        _count = defaultdict(int)
        for emp in self._team:
            _count[emp[2]] += 1
        return _count

# Analysis of employees.csv file
with open('apple_employees.csv') as f:
    apple = Company()
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        apple.add_emp(row[0], row[1], row[2], row[3])

print(apple.total_cost())
print(apple.emp_count_by_gender())
print(apple.emp_count_by_department())

# ================================================================
class Covid:
    def __init__(self):
        self.records = []

    def add_case(self, country, _date, cases):
        self.records.append({"country": country, "_date": _date, "cases": int(cases)})

    def total_cases(self):
        return sum([record['cases'] for record in self.records])

    def cases_by_country(self):
        from collections import defaultdict
        d = defaultdict(int)
        for record in self.records:
            d[record['country']] += record['cases']
        return d


with open('covid_data.csv', 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)    # Skipping Headers
    c = Covid()
    for row in rows:
        c.add_case(row[2], row[3], row[5])
    print(c.total_cases())
    print(c.cases_by_country())
