"""
1. A class is collection/set of functions that carry out various operations on 
"Instances"

2. Instances are the actual objects/data that your function manipulate on.
"""
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def move(self, dx, dy):
        self.a += dx
        self.b += dy

p1 = Point(1, 2)
p2 = Point(10, 20)

print(p1.__dict__)  # {"a": 1, "b": 2}
print(p2.__dict__)  # {"a": 10, "b": 20}

class Point:
    # a and b with default values
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

p1 = Point()
p2 = Point()

class Employee:
    def __init__(self, fname, lname, pay, *args):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.args = args

e1 = Employee('steve', 'jobs', 1000, 'python', 26, '2200 valley view lane')

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

"""
1. Internally all the instance attributes are stored in a Instance Dictionary.
2. All the methods in the class are stored in Class Dictionary
"""

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

class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        self.amount -= amount

    def balance(self):
        print(self.amount)

b1 = BankAccount("steve", 1000)
b2 = BankAccount("bill", 2000)