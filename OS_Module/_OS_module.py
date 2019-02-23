import os

print(os.getcwd())  # Prints current working directory

os.chdir(r'C:\Users\ssuryaprasad\Desktop')     # Changes the working directory

print(os.listdir)     # Lists all available files and folders in the current working directory

try:
    os.makedirs(r'hello_testing')     # Creates directories (Multiple directories)
except FileExistsError as e:
    print(e)

os.removedirs(r'hello_testing')     # Removes directories

os.rename('test.txt', 'testing.txt')    # Renames the file

os.chdir(r'C:\Users\ssuryaprasad\Desktop\hello_testing')

files = os.listdir()

for file in files:
    temp_file_name, file_ext = os.path.splitext(file)
    file_name, file_number = temp_file_name.split('#')
    new_file_name = f'{file_number.zfill(2)}-{file_name}.{file_ext}'
    os.rename(file, new_file_name)

# Determine if any .py files exist in a directory
my_dir = os.getcwd()
names = os.listdir(my_dir)

pyfiles = [name for name in os.listdir(my_dir) if name.endswith('.py')]
others = [name for name in os.listdir(my_dir) if not name.endswith('.py')]

# Testing the existance of files and directories
print(os.path.exists('testing.txt'))    # Prints True if the file exists.

print(os.path.isfile('testing.txt'))    # Prints True if it is file

print(os.path.isdir(r'C:\Users\ssuryaprasad\Desktop\hello_testing'))    # Prints True if it is a Directory