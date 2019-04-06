# Object oriented programing
class Employee:
    no_emps = 0     # Class Variable

    def __init__(self, fname, lname, pay):
        self.fname = fname.title()
        self.lname = lname.title()
        self.pay = pay
        self.email = fname.title() + '.' + lname.title() + '@company.com'
        Employee.no_emps += 1

    def full_name(self):
        return f'{self.fname.title()} {self.lname.title()}'

    def emp_email(self):
        return self.email
    
    @classmethod
    def empid(cls):
        return cls.no_emps


e1 = Employee('robert', 'hunter', 90000)
e2 = Employee('laura', 'turner', 80000)
e3 = Employee('lee', 'martin', 70000)
e4 = Employee('amy', 'masters', 60000)

print(e1.full_name())   # Prints the full name of the employee. self argument is passed automatically
print(Employee.full_name(e1))   # Prints full name of the employee. self argument should be passed explicitly.


class Developer(Employee):
    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, fname, lname, pay, employees):
        super().__init__(fname, lname, pay)
        self.employees = employees
    
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
dev3 = Developer('dave', 'laurs', 50000, 'Oracle')
dev4 = Developer('steve', 'williams', 80000, 'C++')
print(dev1.full_name())
print(dev1.emp_email())
print(dev1.prog_lang)
print(dev2.prog_lang)

mg1 = Manager('Sue', 'Smith', 90000, [dev1, dev2])
# mg1.add_employee([dev1, dev2, dev3, dev4])
mg1.print_emp()
print()
mg2 = Manager('Steve', 'Jobs', 80000, [dev3, dev4])
# mg2.add_employee([dev3, dev4])
mg2.print_emp()
