import csv


class Portfolio:
    value = 100

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


filename = 'portfolio.csv'
types = [str, int, float]
records = []


def read_csv(filename, types):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skipping headers
        for row in rows:
            converted = [func(val) for func, val in zip(types, row)]
            name, shares, price = converted
            records.append(Portfolio(name, shares, price))
    return records


data = read_csv(filename, types)


def print_table(objects, colnames):
    for col in colnames:
        print(f'{col:>10}', end='')
    print()

    for obj in objects:
        for col in colnames:
            print(f'{getattr(obj, col):>10}', end='')
        print()


print_table(data, ['price', 'shares', 'name'])