import heapq

# Custom Sorting
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

# Sorting the list based on the number of characters of the list item
print(sorted(names, key=lambda name: len(name)))

# Sorting the list based on the last character of the list item
print(sorted(names, key=lambda name: name[-1]))


# Sorting Employee Class
class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def __repr__(self):
        return f'({self.fname}, {self.lname}, {self.salary})'

    def full_name(self):
        return self.fname + ' '+ self.lname

    def email(self):
        return f'{self.fname}.{self.lname}@company.com'


emp1 = Employee('steve', 'jobs', 90000)
emp2 = Employee('bill', 'gates', 80000)
emp3 = Employee('joseph', 'trev', 70000)

li_emp = [emp1, emp2, emp3]

print(sorted(li_emp, key=lambda emp: emp.salary))

print(heapq.nlargest(2, [(emp.salary, emp.full_name()) for emp in li_emp]))
print(heapq.nsmallest(2, [(emp.salary, emp.full_name()) for emp in li_emp]))
