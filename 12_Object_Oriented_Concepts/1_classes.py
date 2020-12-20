import datetime
import time
import csv

# A class is collection/set of functions that carry out various operations on
# "Instances"

# Instances are the actual objects/data that your function manipulate on.
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

# Company Class.
class Company:
    def __init__(self):
        self._team = []

    # Alternate Constructor Mechanism
    @classmethod
    def from_csv(cls):
        c = cls()
        with open('data/employees.csv') as f:
            rows = csv.reader(f)
            next(rows)
            for row in rows:
                c._team.append((row[0], row[1], row[2], row[3]))
        return c

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

    @classmethod
    def from_csv(cls):
        c = cls()
        with open('_covid_data.csv', 'r') as f:
            rows = csv.reader(f)
            headers = next(rows)    # Skipping Headers
            for row in rows:
                c.add_case(row[0], row[1], row[2])
        return c

    def total_cases(self):
        return sum([record['cases'] for record in self.records])

    def cases_by_country(self):
        from collections import defaultdict
        d = defaultdict(int)
        for record in self.records:
            d[record['country']] += record['cases']
        return d


with open('_covid_data.csv', 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)    # Skipping Headers
    c = Covid()
    for row in rows:
        c.add_case(row[0], row[1], row[2])
    print(c.total_cases())
    print(c.cases_by_country())
