from itertools import count
import time

'''
1. A Generator is a function that returns an iterator. It generates values using the 'yield' keyword.
2. They don't take memory of a list. They are LAZY Iterables. Generators are used for saving memory.
3. when called on next() function a raises StopIteration exception when there are no more values to generate.
4. 'yield' keyword suspends or pauses the execution of the function. But 'return' statement ends the function.
'''
# Simple Generator
def func():
    print('Hello')
    yield "Hi"
    print('World')
    yield "Bye"

# Countdown Generator
def countdown(start):
    print('Starting countdown from ', start)
    while start > 0:
        yield start
        start -= 1
    print('Done!')

# Generates a range of floating point numbers
def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step

# Generator produces even numbers
def evens(iterable):
    print('Genertor Wakes up!!')
    for item in iterable:
        if item % 2 == 0:
            yield item
            print("Runing After Yield")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e = evens(a)
c = count()     # Create a count object
i = evens(c)    # passing an infinite iterable to evens func

# Generator Expression
evens = (item for item in a if item % 2 == 0)

# Generator which ignores commented lines and yields only actual lines of code
def actual_lines():
    with open('code.txt') as f:
        for line in f:
            if not line.strip():
                continue
            if line.startswith('#'):
                continue
            yield line


# Generator Expression!
g_actual_lines = (line for line in open('code.txt') if not line.startswith('#') and line.strip())

# Generator which yeild words in a sentence
sentence = "Hello world welcome to Python"
def g_words(sentence):
    words = sentence.split()
    for word in words:
        yield word

# Write a generator function which yields a line from a log file, if the line has "EVENT" string in it
def g_lines():
    with open('errors.log') as f:
        for line in f:
            if 'EVENT' in line:
                yield line

g = g_lines()
for line in g:
    print(line)

# Generator Expression for the above problem
lines = (line for line in open("Data/sample.log") if "EVENT" in line)

for line in lines:
    print(line)

# Function that reads entire contents of file to a list
def read_log():
    with open('data/airline.log') as f:
        return f.readlines()

# Generator that produces one line when asked for it
def g_read_log():
    with open('data/errors.log') as f:
        for line in f:
            yield line

# Generator that searches for a partucular pattern
def _grep(pattern, line):
    if pattern in line:
        yield line

lines = read_log()
for line in g_read_log():
    for match in _grep('WARN', line):
        print(line)
        time.sleep(1)

# Monitering live log file using generators
def _tail():
    with open('/var/logs/system.log') as log:
        log.seek(0, 2)   # Goes to End of File
        while True:
            line = log.readline()
            if not line.strip():
                time.sleep(0.1)
                continue
            yield line
