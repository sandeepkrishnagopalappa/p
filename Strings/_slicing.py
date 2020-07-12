# String Slicing
# my_message[start:stop:step]
my_message = 'Hello World'
print(my_message[0])        # Prints the character present at the 0th index
print(my_message[10])       # Prints the character present at the 10th index
print(my_message[0:5])      # Prints Hello. Upto 5th character, but NOT INCLUDING the 5th
print(my_message[:5])       # Prints Hello.
print(my_message[6:])       # Prints World

print(my_message[:5] + my_message[5:])

# Inserting white space between the strings
fullname = 'stevejobs'
print(fullname[:5].capitalize() + ' ' + fullname[5:].capitalize())

sample_url = 'http://apple.com'
print(sample_url[-3:])