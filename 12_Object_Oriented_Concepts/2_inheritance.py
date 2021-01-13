from itertools import count
from datetime import datetime

class Parent:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print('Parent.Apple', self.value)

    def google(self):
        print('Parent.Google')
        self.apple()


class Child1(Parent):
    def yahoo(self):        # Completely Independent Method
        print('Child1.Yahoo')


class Child2(Parent):
    def apple(self):        # Overriding Parent class Method
        print('Child2.Apple', self.value)


class Child3(Parent):
    def apple(self):        # Overriding Parent class Method but reusing the original method in Parent
        print('Child2.Apple')
        super().apple()


class Child4(Parent):
    def __init__(self, value, extra):   # Adding a new Attribute
        self.extra_value = extra
        super().__init__(value)


class Parent2:
    def facebook(self):
        print('Parent2.Facebook')


class Child5(Parent, Parent2):  # Child Inheriting from more than one parent
    pass


# Method Resolution Order - MRO
c = Child5(10)
print(c.__class__.__mro__)

# Advanced Inheritance
class Parent:
    def spam(self):
        print('Parent Spam')

class Child1(Parent):
    def spam(self):
        print('Child1.Spam')
        super().spam()

class Child2(Parent):
    def spam(self):
        print('Child2.Spam')
        super().spam()

class Child3(Child1, Child2):
    pass

# Calculating Payroll of different Employees
class Employee:
    def __init__(self, _id, name):
        self._id = _id
        self.name = name


class WeeklyEmployee(Employee):
    def __init__(self, _id, name, weekly_salary):
        self.weekly_salary = weekly_salary
        super().__init__(_id, name)

    def calculate_pay(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, _id, name, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        super().__init__(_id, name)

    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate


class CommisionedEmployee(WeeklyEmployee):
    def __init__(self, _id, name, weekly_salary, commision):
        self.commision = commision
        super().__init__(_id, name, weekly_salary)

    def calculate_pay(self):
        fixed_pay = super().calculate_pay()
        return fixed_pay + self.commision


# Function that calculates the pay of all Employees
def calculate_payroll(employess):
    print('Calculating Payroll')
    for employee in employess:
        print(f'Pay for {employee._id}, {employee.name} = {employee.calculate_pay()}')


e1 = HourlyEmployee('1', 'steve', 40, 20)
e2 = WeeklyEmployee('2', 'Bill', 1250)
e3 = CommisionedEmployee('3', 'John', 1250, 100)
calculate_payroll([e1, e2, e3])


# Custom Exceptions for Bank Transactions!!
class TransactionDeclined(Exception):
    pass


class InsufficientBalance(Exception):
    pass


class MaxWithdrawLimtExceeded(Exception):
    pass


class BankAccount:
    interest_rate = 4.0

    def __init__(self, fname, lname, amount):
        self.fname = fname
        self.lname = lname
        self.balance = float(amount)
        self._transactions = []
        self._transactions.append(f"{datetime.now()} ***Initial Deposit*** {self.amount}")

    def deposit(self, amount):
        self.balance += float(amount)
        self._transactions.append(f'{datetime.now()} Deposited Amount: {amount}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self._transactions.append(f'{datetime.now()} Withdrawn Amount: {amount}')
        else:
            raise InsufficientBalance()

    def statement(self):
        for line in self._transactions:
            print(line)
        print(f"Total Account Balance: {self.balance}")

    def roi(self):
        self.balance = self.balance + self.balance * (self.interest_rate / 100)


class SavingsAccount(BankAccount):
    interest_rate = 4.0

    def withdraw(self, amount):
        if amount > 10000:
            raise MaxWithdrawLimtExceeded('Can not withdrawn more than 10000 per day')
        super().withdraw(amount)


class SalaryAccount(BankAccount):
    def __init__(self, fname, lname):
        self.isFirstTime = True
        self._draft_amount = 0.00
        super().__init__(fname, lname, 0.00)

    def deposit(self, amount):  # Add A/C opening Bonus of 1000rs
        if self.isFirstTime:
            self.balance += 1000
            self.isFirstTime = False
        super().deposit(amount)

    def overdraft(self, amount):
        if self._draft_amount <= 10000:
            self.balance += amount
            self._draft_amount += amount
            self._transactions.append(f'{datetime.now()} ***Overdraft Amount Credited*** {amount}')
        else:
            raise Exception


class SeniorCitizenAccount(BankAccount):
    interest_rate = 5.5

    def withdraw(self, amount):
        if amount > 20000:
            raise MaxWithdrawLimtExceeded('Can not withdraw more than 20000 per day')
        super().withdraw(amount)


class SukanyaSamrudhiAccount(BankAccount):
    interest_rate = 9.5

    def deposit(self, amount):
        if amount < 1000:
            raise ValueError('Min Amount Should be 1000rs')
        super().deposit(amount)

    # Completely overriding the parent class method "withdraw"
    def withdraw(self, amount):
        raise TransactionDeclined("Can not withdraw")


class PenaltyAccount:
    def withdraw(self, amount):
        self.balance -= 200  # Penalty for withdrawing from PensionAccount
        super().withdraw(amount)


class RetirementAccount(PenaltyAccount, BankAccount):
    pass