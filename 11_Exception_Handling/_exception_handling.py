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


print(factorial(5))


def div(a, b):
    return a / b


try:
    print(div(1, 0))
    print('Running Try Block')      # Never executes if there is any exception in div function
except FileNotFoundError as e:
    print(e)
else:           # Else Block Runs only if there is no exception in try block
    print('Running Else Block')
finally:        # Finally Block Runs regardless of what happens in try and except block
    print('Running finally')    # Always executes no matter what happens in try/except/else block

print('Hello world')    # Never executes if there is any exception in try block


# Defining Custom Exceptions
class NetworkError(Exception):
    pass


class DeviceError(Exception):
    pass


raise DeviceError('Device Not Responding')

raise NetworkError("Can not find the Host")
