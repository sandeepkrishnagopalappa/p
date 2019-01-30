import heapq

# List Comprehensions are used for building a new list

# Square Numbers in the list. Using 'for' loop
nums = [1, 2, 3, 4, 5]
squares = []
for num in nums:
    squares.append(num ** 2)

# Square Numbers in the list. Using List Comprehensions
list_evens = [num ** 2 for num in nums]
print(list_evens)

# Reverse of list difference
reverse_difference = [
    n1 - n2
    for n1, n2 in zip(nums, nums[::-1])
]
print(reverse_difference)

# Dictionary Comprehension
sentence = '''Python is an easy to learn, powerful programming language. 
It has efficient high-level data structures and a simple but effective approach to object-oriented programming.
Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language 
for scripting and rapid application development in many areas on most platforms.'''
dict_word_count = {
    word: sentence.count(word)
    for word in sentence.split(' ')
}
print(dict_word_count)

# Dictionary of character and ascii value pairs
s = 'abcABC'
dict_ascii = {
    c: ord(c)
    for c in s
}
print(dict_ascii)

# Returns a list containing all vowels in the given string
my_string = 'Hello world'
vowels = [
    c
    for c in my_string
    if c in ['a', 'e', 'i', 'o', 'u']
]
print(vowels)


# Counts the occurance of each word in the text file and prints the most and least repeated words
with open('read.txt', 'r') as f:
    text = f.read()
    d = {word: text.count(word) for word in text.split(' ')}

print('Original dictionary --->', d)

print(heapq.nlargest(3, d.items(), key=lambda name: name[-1]))

print(heapq.nsmallest(3, d.items(), key=lambda name: name[-1]))
