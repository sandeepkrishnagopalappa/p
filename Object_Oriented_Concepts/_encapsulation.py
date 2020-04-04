class A:
    def __init__(self):
        self._internal = 0  # An internal/private attribute
        self.public = 1   # A Public attribute

    def public_method(self):
        print('Public method')
        return self._internal

    def _private_method(self):
        print('Internal Method')


class B:

    def __init__(self):
        super().__init__()
        self.__internal = 1     # Double underscores are used to hide internal attributes
        # of the class when the class gets inherited

    def public_method(self):
        return self.__internal


class C(B):

    def __init__(self):
        super().__init__()
        self.__internal = 2     # Does not override B.__internal

    def public_method(self):
        return self.__internal


b = B()
c = C()

print(b.public_method())
print(c.public_method())


# ====================================================================================

# Setters and Getters

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        # By setting self.first_name , the set operation uses the setter method to set the
        # first_name attribute as opposed to bypassing it by accessing self._first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('First Name must be String')
        if len(value) > 12:
            raise ValueError('First Name must be less than 13 characters')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


p1 = Person('Steve', 'Jobs', 30)


print(p1.first_name)

p1.first_name = 'Bill'

print(p1.first_name)

# del p1.first_name


# Imlementation of properties Using Descriptors
class Descriptor:
    def __init__(self, value):
        self.value = value

    def __set__(self, instance, newvalue):
        instance.__dict__[self.value] = newvalue

class TypeCheck(Descriptor):
    expected_type = None
    def __set__(self, instance, newvalue):
        if not isinstance(newvalue, self.expected_type):
            raise TypeError(f'Expected Type should be {self.expected_type}')
        super().__set__(instance, newvalue)

class Integer(TypeCheck):
    expected_type= int


class String(TypeCheck):
    expected_type = str


class Float(TypeCheck):
    expected_type = float


class Positive(Descriptor):
    def __set__(self, instance, newvalue):
        if newvalue < 0:
            raise ValueError('Cant be Negative')
        super().__set__(instance, newvalue)

class Sized(Descriptor):
    def __init__(self, value, *, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(value, **kwargs)

    def __set__(self, instance, value):
        if len(value) > self.maxlen:
            raise ValueError('Can not be more than 10 chars')
        super().__set__(instance, value)

class Regx(Descriptor):
    def __init__(self, value, *, pat):
        self.pat = pat
        super().__init__(value)

    def __set__(self, instance, value):
        import re
        matches = re.compile(self.pat)
        print(matches)
        super().__set__(instance, value)


class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class SizedString(String, Sized):
    pass

class SizedRegxString(SizedString, Regx):
    pass


class Employee(object):
    firstname = SizedRegxString("firstname", maxlen=10, pat='[A-Z]+')
    lastname = SizedRegxString("lastname", maxlen=10, pat='[A-Z]+')
    age = PositiveInteger('age')

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


e1 = Employee('Steve', 'Jobs', 40)
e2 = Employee('Bill', 'Gates', 41)
