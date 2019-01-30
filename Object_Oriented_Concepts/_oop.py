# Object oriented programing
class Employee:
    no_emps = 0     # Class Variable

    def __init__(self, fname, lname, salary):
        self.fname = fname.title()
        self.lname = lname.title()
        self.salary = salary
        Employee.no_emps += 1

    @property
    def full_name(self):
        return f'{self.fname.title()} {self.lname.title()}'

    @property
    def email(self):
        return f'{self.fname.title()}.{self.lname.title()}@dxc.com'

    @property
    def empid(self):
        return Employee.no_emps


e1 = Employee('robert', 'hunter', 90000)
e2 = Employee('laura', 'turner', 80000)
e3 = Employee('rob', 'shrimpton', 70000)
e4 = Employee('bucky', 'roberts', 60000)

emp_list = [e1, e2, e3, e4]




