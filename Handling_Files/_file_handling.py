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

