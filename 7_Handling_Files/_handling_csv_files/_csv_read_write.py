import csv
from collections import defaultdict

# Reading CSV Files
with open('portfolio.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)     # Prints each line of csv file.

with open('portfolio.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line[0], line[1])     # Prints only first and second column.

with open('portfolio.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line['name'], line['shares'])


# Writing to CSV Files
with open('new_portfolio.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['name', 'shares', 'price'])


with open('portfolio.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, ['name', 'shares', 'price'])
    csv_writer.writeheader()
    csv_writer.writerow({'name': 'IBM', 'shares': 100, 'price': 65.3})


data = [('apple', 'google', 'yahoo'), ('microsoft', 'netflix', 'gmail')]
with open('company.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)  # Write rows takes a list of iterables

# Reading csv file into a data structure
_portfoilo = []
types = [str, int, float]
# converted = [func(val) for func, val in zip(types, row)]
# name, shares, price = converted
with open('portfolio.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        record = {
                  'name': row[0],
                  'shares': int(row[1]),
                  'price': float(row[2])
                  }
        _portfoilo.append(record)

print(_portfoilo)   # List of Dictionaries

# Finding the total
total = 0.00
for holding in _portfoilo:
    total += holding.get('price')
print(total)

# Shares holding greater than 100
for holding in _portfoilo:
    if holding.get('shares') > 100:
        print(holding)

# Prices of shares with greater than $100
for holding in _portfoilo:
    if holding.get('price') > 100:
        print(holding)

# Finding min and max price of all the stocks
prices = []
for holding in _portfoilo:
    prices.append(holding.get('price'))

print(min(prices))
print(max(prices))

# Reading CSV rows as columns
cols = defaultdict(list)

def read_columns(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            for header, r in zip(headers, row):
                cols[header].append(r)
    return cols

print(read_columns('portfolio.csv'))