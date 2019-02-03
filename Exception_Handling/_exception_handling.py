
# Handling exception while reading from file

try:
    file = open('read.txt')
except FileNotFoundError as e:
    print(e)
else:           # Else Block Runs only if there is no exception in try block
    print(file.read())
finally:        # Finally Block Runs regardless of what happens in try and except block
    print('Running finally')
    

# Handling divide by zero exception
def divide(number):
    try:
        result = 1 / number
    except ZeroDivisionError as e:  # The Scope of e is only inside except block
        print(e)
    except TypeError as e:
        print(e)
    else:
        return result


print(divide(0))    # Raises divide by zero exception
print(divide(2))  # Raises Type error


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
