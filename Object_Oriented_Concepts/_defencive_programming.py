from abc import ABC, abstractmethod


class Bank(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def statement(self):
        pass


class Citi(Bank):
    def __init__(self, amount):
        super().__init__(amount)

    def deposit(self):
        print('Depositing Amount to Citi Bank')

    def withdraw(self):
        print('Withdrawing Amount from Citi Bank')

    def statement(self):
        print('Printing Citi Bank Statement')


class Sbi(Bank):
    def __init__(self, amount):
        super().__init__(amount)

    def deposit(self):
        print('Depositing Amount to SBI Bank')

    def withdraw(self):
        print('Withdrawing Amount from SBI Bank')

    def statement(self):
        print('Printing SBI Bank Statement')


class Hdfc(Bank):
    def __init__(self, amount):
        super().__init__(amount)

    def deposit(self):
        print('Depositing Amount to HDFC Bank')

    def withdraw(self):
        print('Withdrawing Amount from HDFC Bank')

    def statement(self):
        print('Printing HDFC Bank Statement')


def bank_transactions(transaction_name, *args, **kwargs):
    transaction_name(*args, **kwargs)

b = Hdfc(1000)
bank_transactions(b.deposit, 1000)


