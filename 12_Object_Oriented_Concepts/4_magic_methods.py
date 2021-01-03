import csv

x = 10

x.__add__(10)

x.__mul__(10)

x.__sub__(10)

names = ['apple', 'google', 'yahoo']

names.__getitem__(0)    # Same as names[0]

names.__setitem__(1, 'facebook')    # Same as names[1] = "facebook"

names.__contains__("apple")     # Same as "apple" in names


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._points = (a, b)

    # Making Object Printable
    def __str__(self):
        return f"({self.a},{self.b})"

    # Implementing length of the object
    def __len__(self):
        return len(self._points)

    # Making an object iterable
    def __iter__(self):
        return iter([i for i in self._points])

    # Implementing membership operator
    def __contains__(self, item):
        return item in self._points

    # Making an object indexable!
    def __getitem__(self, item):
        return self._points[item]

    # Restricting adding new attribute to the class
    def __setattr__(self, name, value):
        print('Setting Attribute')
        if name not in {"a", "b", "points"}:
            raise AttributeError(f"Cannot Add new Attribute {name}")
        super().__setattr__(name, value)

    # Checks if two Point objects are equal
    def __eq__(self, other):
        return (self._points) == (other._points)

    def __gt__(self, other):
        return sum(self._points) > sum(other.points)


# Implementing magic methods on Company class
class Company:
    def __init__(self):
        self._team = []

    def __iter__(self):
        return iter(self._team)

    def __len__(self):
        return len(self._team)

    def __getitem__(self, index):
        return self._team[index]

    @classmethod
    def from_csv(cls):
        c = cls()
        with open('data/apple_employees.csv') as f:
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