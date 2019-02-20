# BOOLEANS
# Python evaluates below conditions to False
# False
# None
# Zero
# Any empty sequence. e.g. '', (), []
# Any empty mapping {}

condition = ''

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

# and
# or
# not
# is

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Invalid Credentials!!!')

if not logged_in:
    print('Please login')
else:
    print('Welcome!')

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # Evaluates to True
print(a is b)   # Evaluates to False    id(a) == id(b)

c = a

print(a == c)   # Evaluates to True
print(a is c)   # Evaluates to True