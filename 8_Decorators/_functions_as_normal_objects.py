i = 1

f = 1.2

b = True

l = [1, 2, 3]

d = {'a': 1, 'b': 2}

s = {1, 2, 3}

t = (1, 2, 3)


def greeting():
    print('Hello world')


def func(something):
    return something


# Appending a function to a list
l.append(greeting)

# Adding a function to dictionary
d.update({'greeting': greeting})
