import datetime
import time

# A class defines a set of attributes associated with a collection of objects known as
# instances.These attributes typically include functions, which are known as methods, vari-
# ables, which are known as class variables, and computed attributes, which are known as
# properties.
# Object oriented programing


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

class Employee:
    no_emps = 0     # Class Variable
    company_name = 'Apple.Inc'

    def __init__(self, fname, lname, pay):
        self.fname = fname.title()
        self.lname = lname.title()
        self.pay = int(pay)
        self.email = f'{self.fname}.{self.lname}@company.com'
        Employee.no_emps += 1

    def full_name(self):
        return f'{self.fname.title()} {self.lname.title()}'

    def emp_email(self):
        return self.email
    
    @classmethod
    def empid(cls):
        return cls.no_emps

    @classmethod    # Class Methods can be used as alternate constructors
    def emp_from_string(cls, s):
        fname, lname, pay = s.split(',')
        return cls(fname, lname, pay)

    @staticmethod
    def just_function_inside_class():
        print('Hello world')


# One use if cls is in Inheritance:
class NewEmployee(Employee):
    pass


n = NewEmployee.emp_from_string('steve,jobs,1000')

e1 = Employee('robert', 'hunter', 90000)
e2 = Employee('laura', 'turner', 80000)
e3 = Employee('lee', 'martin', 70000)
e4 = Employee('amy', 'masters', 60000)


e = Employee.emp_from_string('steve, jobs, 9000')   # Alternate method of emp instance

print(e1.full_name())   # Prints the full name of the employee. self argument is passed automatically
print(Employee.full_name(e1))   # Prints full name of the employee. self argument should be passed explicitly.

getattr(e, 'fname')     # Same as e.fname
getattr(e, 'lname')     # Same as e.lname
setattr(e, 'fname', 'Steve')    # Same as e.fname = 'Steve'


class Developer(Employee):
    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        self.employees = list(employees) if employees else []
        # By Casting employees to list, the user has flexibility to pass any iterable.
    
    def add_employee(self, employees):
        for emp in employees:
            if emp not in self.employees:
                self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print(emp.full_name())


dev1 = Developer('test', 'user', 70000, 'Python')
dev2 = Developer('david', 'bob', 60000, 'Java')
dev3 = Developer('dave', 'laura', 50000, 'Oracle')
dev4 = Developer('steve', 'williams', 80000, 'C++')
print(dev1.full_name())
print(dev1.emp_email())
print(dev1.prog_lang)
print(dev2.prog_lang)

mg1 = Manager('Sue', 'Smith', 90000, [dev1, dev2])
# mg1.add_employee([dev1, dev2, dev3, dev4])
mg1.print_emp()
print()
mg2 = Manager('Steve', 'Jobs', 80000, (dev3, dev4))
# mg2.add_employee([dev3, dev4])
mg2.print_emp()
# ================================================================
