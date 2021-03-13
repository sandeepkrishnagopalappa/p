import csv
# Handling exception while reading from file
try:
    file = open('read.txt')
except FileNotFoundError as e:
    print(e)
else:           # Else Block Runs only if there is no exception in try block
    print(file.read())
finally:        # Finally Block Runs regardless of what happens in try and except block
    print('Running finally')

# Handling Bad records in csv file.
total = 0.00
with open('portfolio.csv', 'r') as f:
    next(f)     # Skip the header
    rows = csv.reader(f)
    for lineno, row in enumerate(rows):
        try:
            total += float(row[2])
        except ValueError as err:
            print('Line:', lineno, ':', err)
            continue

print('Total value of stock is :', total)

names = ["apple", "google", "yahoo", "yahoo", "gmail", "apple", "apple", "apple"]
_counts = {}
for c in _counts:
    try:
        _counts[c] = _counts[c] + 1
    except KeyError:
        _counts[c] = 1

# Handling Divide by Zero exception.
def func(n1, n2):
    try:
        result = n1 / n2
    except ZeroDivisionError:
        print("Bad Record:",(n1, n2))
    else:
        print(result)
    finally:
        print('Executing Finally')

numbers = [(1, 0), (3, 4), (4, 5), (1, 0), (3, 4), (3, 0)]

for number in numbers:
    n1, n2 = number
    func(n1, n2)

# Raising exceptions
def factorial(n):
    if isinstance(n, str):
        raise TypeError('No String value accepted')
    if n < 0:
        raise ValueError('Value should be greater than or equal to Zero')
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def func():
    try:
        print('Executing Try Block')
    except:
        print("Executing Except Block")
    # else block gets executed only when there is no exception in try block.
    else:
        print('Executing Else Block')
    # finally gets executed no matter what happens in try, except and else blocks.
    finally:
        print('Executing Finally Block')

def func():
    try:
        print('Executing Try Block')
        raise TypeError
    except ValueError:
        print("Catching ValueError")
    except TypeError:
        print('Catching TypeError')
    # else block gets executed only when there is no exception in try block.
    else:
        print('Executing Else Block')
        raise ValueError
    # finally gets executed no matter what happens in try, except and else blocks.
    finally:
        print('Executing Finally Block')

def func():
    try:
        print('Executing Try Block')
    except (ValueError, TypeError, ZeroDivisionError):
        print("Catching ValueError")
    # else block gets executed only when there is no exception in try block.
    else:
        print('Executing Else Block')
        raise AttributeError
    # finally gets executed no matter what happens in try, except and else blocks.
    finally:
        print('Executing Finally Block')

def func():
    try:
       return 1
    except:
        return 2
    else:
        return 3
    finally:
        print('Finaly')

def func():
    try:
       return 1
    except:
        return 2
    else:
        return 3
    finally:
        return 4

# Defining Custom Exceptions
class InsufficientFunds(Exception):
    pass

class AuthError(Exception):
    pass

class NetworkError(Exception):
    pass

def withdraw(amount):
    if amount > 5000:
        raise InsufficientFunds

def login(username, password):
    if username == 'admin' and password == 'admin123':
        print('Login Success')
    else:
        raise AuthError
