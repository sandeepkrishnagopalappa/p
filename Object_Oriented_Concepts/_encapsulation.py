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

# Using Descriptors


class TypeCheck(object):

    def __init__(self, attribute_name, expected_type):
        self.attribute_name = attribute_name
        self.expected_value = expected_type

    def __get__(self, instance, cls):
        return instance.__dict__[self.attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_value):
            raise TypeError(f'{self.attribute_name} should be of {self.expected_value}')
        instance.__dict__[self.attribute_name] = value


class TypeString(TypeCheck):
    def __init__(self, attribute_name, expected_type):
        super().__init__(attribute_name, expected_type)

    def __set__(self, instance, value):
        super().__set__(instance, value)    # Type Check for String
        if len(value) > 10:
            raise ValueError(f'{self.attribute_name} should be less than 10 characters')
        instance.__dict__[self.attribute_name] = value


class TypeInteger(TypeCheck):
    pass


class Employee(object):

    firstname = TypeString('firstname', str)
    lastname = TypeString('lastname', str)
    age = TypeInteger('age', int)

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


e1 = Employee('Steve', 'Jobs', 40)
e2 = Employee('Bill', 'Gates', 41)

