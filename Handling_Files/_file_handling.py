from collections import Counter
from collections import defaultdict
# File Objects

# r ---> Read Only, w ---> Write Only, a ---> Append, r+ ---> Read and Write

# Reading file without using Context manager
f = open('read.txt', 'r')
f_contents = f.read()
print(f_contents)
f.close()

# Reading file Using Context Manager (No need to close the file explicitly when file is opened using contex manager)
with open('read.txt') as f:
    f_contents = f.readlines()   # Returns a List
    for line in f_contents:
        print(line, end='')
    print('Number of lines in the file ', len(f_contents))  # Prints total number of lines in the file

with open('read.txt') as f:
    f_contents = f.read()    # Reads the entire contents of the file into a variable as string
    print(f_contents, end='')

with open('read.txt') as f:
    print(f.readline(), end='')  # Reads one line at a time
    print(f.readline(), end='')
    print(f.readline(), end='')

with open('read.txt') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()

with open('read.txt') as f:
    for line in f:           # Loads only one line at a time and prints the line
        print(line, end='')

# Reading 10 characters at a time
size_to_read = 10
with open('read.txt') as f:
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

# Writing to file
with open('write.txt', 'a') as f:
    f.write('Hello world')
    f.write('\n')

# Working with Multiple Files
with open('from_file.txt', 'r') as wf:
    with open('to_file.txt', 'w') as wt:
        for line in wf:
            wt.write(line)

# Printing the line's with line numbers
with open('from_file.txt') as f:
    for linenumber, line in enumerate(f, start=1):
        print(linenumber, line, end='')

# Reading the file in reversed order
with open('read.txt') as f:
    for line in reversed(list(f)):
        print(line, end='')

# Finding the length of each line in the text file
with open('read.txt') as f:
    for line in f:
        print(len(line))


# Exercises:
# 1. Extracting IP addresses from log file
with open('access-log.txt') as f:
    ip = []
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            ip.append(parts[0])

print('Total IP"s:', len(ip))

for item in ip:
    print(item)

# Using List Comprehension
ip = [line.split()[0] for line in open('access-log.txt') if line.strip()]

for item in ip:
    print(item)

# Using Set Comprehension
unique_ip = {line.split()[0] for line in open('access-log.txt', 'r') if line.strip()}

print(len(unique_ip))

out_file = open('ip_list.txt', 'w')
for item in unique_ip:
    print(item)
out_file.close()

# Extracting Messages from sample.log
with open('sample.log') as log:
    for line in log:
        line = line.strip()
        if line:
            parts = line.split()
            print(parts[2])

# Getting Unique Messages
unique_messages = {line.split()[2] for line in open("sample.log") if line.strip()}
print(unique_messages)
# Counting Number of Messages
messages = defaultdict(int)
with open('sample.log') as log:
    for line in log:
        line = line.strip()
        if line:
            parts = line.split()
            messages[parts[2]] += 1
print(messages)

# Using Counter Object
message_list = [line.strip().split()[2] for line in open('sample.log') if line.strip()]
c = Counter(message_list)
print(c)

# Reading Countries from football.txt
with open('football.txt') as log:
    headers = next(log)     # Skipping Header
    for line in log:
        if line.strip():
            print(line.split()[1])

# Using List Comprehension
countries = [line.strip().split()[1] for line in open("football.txt") if line.strip()]

print(len(countries))

# Getting Unique Countries using set() constructor
unique_countries = set(countries)

print(len(unique_countries))

# Getting Unique Countries using Set Comprehension
set_countries = {line.strip().split()[1] for line in open("football.txt") if line.strip()}

print(len(set_countries))
