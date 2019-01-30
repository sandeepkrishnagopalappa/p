class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname.title()
        self.lname = lname.title()
        self.salary = salary

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