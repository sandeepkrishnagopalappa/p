# File Objects

# r ---> Read Only, w ---> Write Only, a ---> Append, r+ ---> Read and Write

# Reading file without using Context manager
file = open('read.txt', 'r')
f_contents = file.read()
print(f_contents)
file.close()

# Reading file Using Context Manager (No need to close the file explicitly when file is opened using contex manager)
with open('read.txt') as file:
    f_contents = file.readlines()   # Returns a List
    for line in f_contents:
        print(line, end='')
    print('Number of lines in the file ', len(f_contents))  # Prints total number of lines in the file

with open('read.txt') as file:
    f_contents = file.read()    # Reads the entire contents of the file into a variable as string
    print(f_contents, end='')

with open('read.txt') as file:
    print(file.readline(), end='')  # Reads one line at a time
    print(file.readline(), end='')
    print(file.readline(), end='')

with open('read.txt') as file:
    for line in file:           # Loads only one line at a time and prints the line
        print(line, end='')

# Reading 10 characters at a time
size_to_read = 10
with open('read.txt') as file:
    f_contents = file.read(size_to_read)
    print(f_contents, end='')
    f_contents = file.read(size_to_read)
    print(f_contents, end='')

# Writing to file
with open('write.txt', 'a') as file:
    file.write('Hello world')
    file.write('\n')

# Working with Multiple Files
with open('from_file.txt', 'r') as wf:
    with open('to_file.txt', 'w') as wt:
        for line in wf:
            wt.write(line)
