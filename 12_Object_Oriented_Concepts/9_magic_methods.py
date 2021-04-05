import csv

names = ['apple', 'google', 'yahoo']

names.__getitem__(0)    # Same as names[0]

names.__setitem__(1, 'facebook')    # Same as names[1] = "facebook"

names.__getattribute__("append")        # Same as names.append

names.__contains__("apple")     # Same as "apple" in names

names.__len__()     # Sames as len(names)

x = 10

x.__add__(10)

x.__mul__(10)

x.__sub__(10)


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._points = (a, b)

    # String representation of Point Object
    def __str__(self):
        print('Running __str__')
        return f"({self.a},{self.b})"

    # Implementing length of the Point Object
    def __len__(self):
        print('Running __len__')
        return len(self._points)

    # Making an object iterable
    def __iter__(self):
        print('Running __iter__')
        return iter(self._points)

    # Implementing membership operator
    def __contains__(self, item):
        print('Running __contains__')
        return item in self._points

    # Making an object indexable!
    def __getitem__(self, item):
        print('Running __getitem__')
        return self._points[item]

    # If you are trying to set a -ve value, it defaults to zero
    def __setitem__(self, key, value):
        value = max(0, value)
        self.__dict__[key] = value

    # Restricting adding new attribute to the class
    # Override __setattr__ method of object class.
    def __setattr__(self, name, value):
        print('Running __setattr__')
        if name not in {"a", "b", "_points"}:
            raise AttributeError(f"Cannot Add new Attribute {name}")
        # If you are trying to set a -ve value, it defaults to zero
        value = max(0, value)
        super().__setattr__(name, value)

    # Restricting someone from deleting the attribute.
    # Override __delattr__ method of object class.
    def __delattr__(self, name):
        print('Running __delattr__')
        raise AttributeError('Cannot Delete Attribute {}'.format(name))

    # Checks if two Point objects are equal
    def __eq__(self, other):
        print('Running __eq__')
        return self._points == other._points

    # Checks if the first Point object is greater than second Point Object
    def __gt__(self, other):
        print('Running __gt__')
        return sum(self._points) > sum(other.points)

    # Checks if the first Point object is less than second Point Object
    def __lt__(self, other):
        print('Running __lt__')
        return sum(self._points) < sum(other._points)

    # Adds two Point Objects
    def __add__(self, other):
        print('Running __add__')
        return sum(self._points) + sum(other._points)

    # Subtracts two Point Objects
    def __sub__(self, other):
        print('Running __sub__')
        return sum(self._points) - sum(other._points)

# Making an Immutable Class
class Point:
    def __init__(self, x, y):
        super().__setattr__("x", x)
        super().__setattr__("y", y)

    def __setattr__(self, attr, value):
        print('Calling __setattr__')
        raise TypeError

    def __delattr__(self, *args):
        print("Calling __delattr__")
        raise TypeError

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