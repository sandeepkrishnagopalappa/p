class Greeting:
    def __call__(self, name):
        print(f'Hello {name}')

class Spam:
    def __init__(self, a):
        self.a = a

    def __call__(self):
        print('Executing __call__ ',self.a)

class Squares:
    def __init__(self, numbers):
        self.numbers = numbers
        self.squares = []

    def __call__(self):
        for number in self.numbers:
            self.squares.append(number ** 2)
        return self.squares

class Evens:
    def __call__(self, number):
        if number % 2 == 0:
            return True
        else:
            return False

# Class Decorator
class Record:
    def __init__(self, func):
        self.func = func
        self._count = 0

    def __call__(self, *args, **kwargs):
        self._count += 1
        return self.func(*args, **kwargs)