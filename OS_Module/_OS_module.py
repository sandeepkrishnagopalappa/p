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

