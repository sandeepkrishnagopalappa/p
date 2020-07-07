from inspect import getmro


class Parent:
    def __init__(self, name):
        print('Parent.name')
        self.name = name

    def speak(self):
        print('Parent.Speak')

    def sing(self):
        print('parent.sing')
        self.speak()


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)
        print('Child.name')

    def speak(self):        # Overriding parent class speak method
        print('child.speak')    # Adding extra functionality to speak method
        super().speak()     # Invoking parent class (original) speak method


class Child2(Parent):
    def __init__(self, name, play):     # Adding extra attribute to the Child class
        super().__init__(name)
        self.play = play


c1 = Child('Steve')
c1.speak()

c2 = Child2('Steve', 'Hop')
c2.speak()

print(Child2.__mro__)   # Prints Method Resolution Order for Class Child2
print(getmro(Child2))   # Prints Method Resolution Order for Class Child2
