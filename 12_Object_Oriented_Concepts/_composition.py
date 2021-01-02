class Engine:
    def __init__(self, ncylinders, bhp):
        self.bhp = bhp
        self.ncylinders = ncylinders

    def start(self):
        print('Engine Started')

    def stop(self):
        print('Engine Stopper')

    def accelerate(self):
        print('Accelerating Engine')


class Car:
    def __init__(self, model, color, year, engine):
        self.model = model
        self.color = color
        self.year = year
        self.engine = engine

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def accelerate(self):
        self.engine.accelerate()


toyota = Car('Innova', 'White', 2020, Engine(4, 147))
hyundai = Car('Creta', 'Black', 2020, Engine(4, 123))


# Stack
class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

# It makes no-sense for Calculator class to inherit from Stack class
# So the Functionality Push and Pop are being deligated to Stack class
class Calculator:
    def __init__(self, stack):
        self._stack = stack

    # Implementation Deligated to Stack Class
    def push(self, item):
        self._stack.push(item)

    # Implementation Deligated to Stack Class
    def pop(self):
        return self._stack.pop()

    def add(self):
        left = self.pop()
        right = self.pop()
        print(left + right)


c = Calculator(Stack())
c.push(1)
c.push(2)
c.add()