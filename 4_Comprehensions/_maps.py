nums = [1, 2, 3, 4, 5]

# Square Numbers in the list. Using map function
def squares(item):
    return item ** 2
list_evens = map(squares, nums) # map returns a map object

for number in list_evens:
    print(number)

# List of even numbers between range 1-50
def evens(item):
    if item % 2 == 0:
        return item

even_numbers = map(evens, range(1, 51))

# Convert to upper case
sentence = "This is bunch of words"

def _upper(item):
    return item.upper()

ucase = map(_upper, sentence.split())

# Build a list of tuples with string and its length pair
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

def len_item_pair(item):
    return (item, len(item))

pairs = map(len_item_pair, names)

print(list(pairs))
