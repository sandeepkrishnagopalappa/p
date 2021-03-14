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