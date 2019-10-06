import csv

x = 10

x.__add__(10)

x.__mul__(10)

x.__sub__(10)

names = ['apple', 'google', 'yahoo']

names.__getitem__(0)

names.__setitem__(1, 'facebook')


class Employee:
    employees = []

    def __init__(self, fname, lname, salary):
        self.fname = fname.title()
        self.lname = lname.title()
        self.salary = salary

    @classmethod
    def from_csv(cls):
        with open('employee.csv', 'r') as f:
            rows = csv.reader(f)
            for row in rows:
                e = Employee(row[0], row[1], row[2])
                cls.employees.append(e)
        return cls.employees

    def full_name(self):
        return f'{self.fname.title()} {self.lname.title()}'

    def email(self):
        return f'{self.fname.title()}.{self.lname.title()}@dxc.com'

    def __repr__(self):
        return f"Employee('{self.fname.title()}', '{self.lname.title()}', '{self.salary}')"

    def __len__(self):
        return len(self.full_name())

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        if self.salary < other.salary:
            return other.salary - self.salary
        return self.salary - other.salary


e1 = Employee('joseph', 'trev', 90000)
e2 = Employee('laura', 'turner', 80000)
e3 = Employee('steve', 'slater', 70000)
e4 = Employee('amy', 'masters', 60000)

emp_list = [e1, e2, e3, e4]

e = Employee.from_csv()

# __repr__ is called
for emp in emp_list:
    print(emp)

# __len__ is called
for emp in emp_list:
    print(len(emp))

# __add__ is called
print(e1 + e2)

# __sub__ is called
print(e2 - e1)