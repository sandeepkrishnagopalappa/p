# Working with Strings or Textaul Data
"""
All Variables should in Lower Case. If there are more than one word in the Variable,
then we separate with under scores. And this is PYTHON CONVENTION
"""
# =================================================================
# Difference ways of constructing a string object
word = 'Hello World'
word = str('Hello world')
print(word)

"""
We can use both single and Double Quotes for the Strings.
If you hava single Quotes in the actual String, we can represent the original String in Double Quotes.
If the String actual String contains Double Quotes, we can use single Quotes to represent the String.
"""

message = "Welcome to Python's world"
print(message)

message = 'Welcome to Pythons"s world'
print(message)

# Both single and double quotes in single sting
message = """ Hello world! "Hi" and 'Bye' """
print(message)

message = ''' Hello world! "Hi" and 'Bye' '''
print(message)

# We can use Escape Charater as well
message = 'Welcome to Python\'s world'
print(message)

message = "Welcome to Python\"s world"
print(message)

# We can use either double backslash or prefix 'r' which stands for raw string or regular expression
print("C:\\testing\\newfolder")
print(r"C:\testing\newfolder")

# use Triple Quotes to represent a Multi-Line String
multi_line_string = '''Hello There..
Welcome to Python tutorials'''
print(multi_line_string)

multi_line_string = """Hello There..
Welcome to Python tutorials"""
print(multi_line_string)

# =========================================================
my_message = 'Hello World'

# Print statement Buffers the output if end parameter is other than \n
print('Hello', end='')
print('World', end='')
print('Welcome', end='')

# String 5_Functions
print(len(my_message))      # Prints the Length of the String. Index starts from Zero
print(my_message.upper())   # Prints the String in Upper Case
print(my_message.lower())   # Prints the String in Lower Case
print(my_message.count('l'))    # Prints number of occurances of the letter 'l'
print(my_message.count('Hello'))    # Prints number of occurances of the word 'Hello'
print(my_message.find('l'))     # Prints the index of first occurance of the letter 'l'
print(my_message.find('World'))     # Prints the index of first occurance of the word 'World'
print(my_message.find('Universe'))      # Prints -1.
print(my_message.replace('World', 'Universe'))  # Prints 'Hello Universe'
print(my_message.split())   # Splits the string based on white space and returns a list

s = 'This is my string'
print(s.split('s'))

s = ' This is my string '   # There is a leading and trailing space
print(s.split(' '))     # Prints ['', 'This', 'is', 'a', 'string', '']

info = '560100, Bangalore, KA'
pin_code, city, state = info.split(',')
print(my_message.startswith('Hello'))
print(my_message.endswith('World'))

my_string = '***************Hello world==================='
print(my_string.rstrip('='))    # prints ***************Hello world
print(my_string.lstrip('*'))    # prints Hello world===================
print(my_string.strip('=*'))    # Prints Hello world

# String Concatination
greeting = 'Hello'
name = 'Steve'
print(greeting, name)

print('Python '+str(2019))      # 2019 should be converted to String if using + operator
print('Python' + ' 2019')
print('Python', 2019)       # Comma is used for concatinating two string of different datatypes

# '+' is used for concatinating two objects of same datatype
print(greeting+', '+name)

# Repeats the string 5 times
print('Hello ' * 5)

# String Conversions
x = 26
print(str(x))   # prints '26'

# Iterating over a string
s = 'hello world'

for c in s:
    print(c)

# Iterating over a part of a string
for c in s[:5]:
    print(c)

# Getting index and item in a string
for index, item in enumerate(s):
    print(index, '---->', item)

# Iterating over multiple string objects using zip function
s1 = 'hello'
s2 = 'world'

for c1, c2 in zip(s1, s2):
    print(c1, c2)