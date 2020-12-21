import csv

x = 10

x.__add__(10)

x.__mul__(10)

x.__sub__(10)

names = ['apple', 'google', 'yahoo']

names.__getitem__(0)

names.__setitem__(1, 'facebook')


class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname.title()
        self.lname = lname.title()
        self.salary = salary

    def full_name(self):
        return f'{self.fname.title()} {self.lname.title()}'

    def email(self):
        return f'{self.fname.title()}.{self.lname.title()}@company.com'

    def __repr__(self):
        return f"Employee('{self.fname.title()}', '{self.lname.title()}', '{self.salary}')"


class Staff:
    def __init__(self):
        self._employees = []

    @classmethod
    def from_csv(cls):
        obj = cls()
        with open('apple_employees.csv', 'r') as f:
            rows = csv.reader(f)
            headers = next(rows)    # Skipping Headers
            for row in rows:
                e = Employee(row[0], row[1], row[2])
                obj._employees.append(e)
        return obj

    def __getitem__(self, index):
        return self._employees[index]

    def __len__(self):
        return len(self._employees)

    def __iter__(self):
        return iter(self._employees)


staff = Staff.from_csv()

# __repr__ is called
for emp in staff:
    print(emp)

# __len__ is called
print(len(staff))

# __iter__ is called
for item in staff:
    print(item)

# __getitem__ is called
print(staff[0])