# Global variable
message = "Hello world"

def func():
    message = "Hello universe"  # Local Variable
    print(message)

def func():
    # Declaring that the variable that you are referring to is global variable
    global message
    message = "Hello Universe"
    print(message)

def demo():
    print(message)  # Prints message at global scope

# Enclosing Scope
def logger():
    message = 'Hello'   # Local Variable for func logger and enclosing for wrapper
    def wrapper():
        message = 'World'   # Local for wrapper
        print(message)
    return wrapper


class Spam:
    message = "Hello world"
    def __init__(self):
        self.message = "Hello universe"

s = Spam()
print(s.message)   # Prints "Hello universe"

class Spam:
    message = "Hello world"
    def __init__(self):
        self.x = 10
        self.y = 20

s = Spam()
print(s.message)    # Prints "Hello world"

def spam():
    # Local Variable "message"!
    # A variable can be either local or global variable but not both
    print(message)
    message = "Hello Universe"
    print(message)

spam()
# Raises Exception!
# (UnboundLocalError: local variable 'message' referenced before assignment)
