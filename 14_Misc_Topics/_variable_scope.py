# x = 'global x'


def test(z):
    global x    # Explicitly declaring x as global inside function
    # y = 'local y'
    # x = 'local x'
    # print(y)
    # print(x)
    print(z)


test('local z')

# print(x)


# Enclosing Scope
def logger():
    message = 'Hello'   # Local Variable for func logger and enclosing for wrapper

    def wrapper():
        message = 'World'   # Local for wrapper
        print(message)
    return wrapper


# global variable
message = "Hello world"

def func():
    # Declaring that the variable that you are referring to is global variable
    global message
    message = "Hello Universe"
    print(message)

def spam():
    # Local Variable "message"!
    print(message)
    message = "Hello Universe"
    print(message)

def demo():
    print(message)
