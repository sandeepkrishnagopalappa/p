def evens(item):
    if item % 2 == 0:
        return item

f = filter(evens, range(1, 10))
print(list(f))  # [2, 4, 6, 8]

# Build a list with only even with even length string using filter func
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

def even_len(item):
    if item % 2 == 0:
        return item

f = filter(even_len, names)
print(list(f))  # ['google', 'facebook', 'yelp', 'flipkart']
