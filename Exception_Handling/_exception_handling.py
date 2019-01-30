try:
    file = open('mailid.txt')
except FileNotFoundError as e:
    print(e)
else:           # Else Block Runs only if there is no exception in try block
    print(file.read())
finally:        # Finally Block Runs regardless of what happens in try and except block
    print('Running finally')

