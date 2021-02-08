# Python evaluates below conditions to False

"""
1. Any Empty String in Python always evaluates to Boolean False.
A non-empty string or a string with atleast one character evaluates to boolean True

2. Any Empty list in python always evaluates to Boolean False.
A Non-Empty list or a list with atleast one item evaluates to Boolean True

3. An Integer Zero in python evaluates to Boolean False
and any number other than zero, it evaluates to Bool True.

4. An Empty Dictionary evaluates to Bool False
and a Dictionary with atleat one key:value pair evaluates to Bool True.

5. An Empty Tuple evaluates to Bool False
and a Tuple with atleast one element evaluates to Bool True.

6. An Empty set() evaluates to Bool False
and a set() with atleast one element evaluates to Bool True

7. None evalutes to Bool False.

8. Bool True evaluates to True and False evaluates to False
"""

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
