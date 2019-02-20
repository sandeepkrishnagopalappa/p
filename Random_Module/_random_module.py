import random

print(random.random())  # Prints a random floating point number between 0 and 1. Both excluding. e.g. 0.1, 0.8

print(random.uniform(1, 10))    # Prints random floating point number between the specified range (1 and 10).

print(random.randint(1, 6))     # Prints random integer between 1 and 6. Both inclusive.

print(random.randrange(0, 100, 5))      # Prints random integer between 0 and 100 with step size of 5

names = ['apple', 'google', 'yahoo', 'facebook', 'microsoft', 'instagram', 'watsapp']

print(random.choice(names))     # Prints a random item in the list 'names'

# Creating a combination of first name and last names from the list
fname = ['steve', 'bill', 'mark', 'rob', 'mike', 'laura', 'adams']
lname = ['jobs', 'gates', 'waugh', 'charlie', 'stone', 'turner', 'randolph']

for _ in range(10):
    full_name = f'{random.choice(fname)} {random.choice(lname)}'
    print(full_name)


# Generating 8 Character random password
random_string = '''
ABEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0987654321!@#$%^()CD_?><&*
'''

password = ''
for _ in range(8):
    password = password + random.choice(random_string)
print(password)
