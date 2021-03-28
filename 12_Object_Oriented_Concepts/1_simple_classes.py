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

    # Class Variable
    interest_rate = 0.04

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []
        self.transactions.append(f'******** Inital Amount Deposit ************ {balance}')

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'Amount deposited: {amount}')

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f'Amount withdrawn: {amount}')

    def transfer(self, to_account, amount):
        if self.balance >= amount:
            to_account.deposit(amount)
            self.balance -= amount
            self.transactions.append(f'NEFT to BankAccount {to_account}')

    def statement(self):
        for item in self.transactions:
            print(item)
        print(f'************ Total Account Balance ********** {self.balance}')

    def roi(self):
        int_amount = self.__class__.interest_rate * self.balance
        self.balance = self.balance + int_amount
        self.transactions.append(f'Interest Amount Credited {int_amount}')

b1 = BankAccount("steve", 1000)
b2 = BankAccount("bill", 2000)

class Covid:
    def __init__(self):
        self.records = []

    def add_case(self, country, _date, cases):
        self.records.append({"country": country, "_date": _date, "cases": int(cases)})

    def total_cases(self):
        return sum([record['cases'] for record in self.records])

    def cases_by_country(self):
        from collections import defaultdict
        d = defaultdict(int)
        for record in self.records:
            d[record['country']] += record['cases']
        return d

    def countries(self):
        return {record['country'] for record in self.records}

# Shopping Cart
class ShoppingCart:
    # Class Variables
    products = {'iPhone': 5, 'iMac': 3, 'iWatch': 2, 'iPad': 4}
    prices = {'iPhone': 800, 'iMac': 2500, 'iWatch': 3000, 'iPad': 3500}

    def __init__(self):
        self.cart = []

    def add_item(self, name, quantity):
        if name not in self.__class__.products.keys():
            raise Exception('Product Not Available')
        elif self.__class__.products[name] >= quantity:
            self.cart.append({'name': name, 'price': self.__class__.prices[name], 'quantity': quantity})
            self.__class__.products[name] -= quantity
        else:
            raise ValueError('Product Out of Stock')

    def total_cost(self):
        return sum([item['price'] * item['quantity'] for item in self.cart])

    def remove_item(self, name):
        for item in self.cart:
            if name == item['name']:
                if item['quantity'] == 1:
                    self.cart.remove(item)
                else:
                    item['quantity'] -= 1

    def summary(self):
        print(f'{"name":>20} {"price":>20} {"quantity":>20}')
        print('-' * 65)
        for item in self.cart:
            print(f'{item["name"]:>20} {item["price"]:>20} $ {item["quantity"]:>20}')
        print('-' * 65)
        print(f'{"Total Cost:":>20}{self.total_cost():>20} $')