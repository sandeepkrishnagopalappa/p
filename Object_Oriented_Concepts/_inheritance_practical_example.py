import csv
from abc import ABC, abstractmethod

class Holding:
    value = 100

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


filename = '/Users/Sandeep/Documents/Python_Practice/data.csv'
types = [str, int, float]
records = []


def read_csv(filename, types):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skipping headers
        for row in rows:
            converted = [func(val) for func, val in zip(types, row)]
            name, shares, price = converted
            records.append(Holding(name, shares, price))
    return records


data = read_csv(filename, types)


def print_table(objects, colnames, formatter):
    formatter.headings(colnames)

    for obj in objects:
        row = [str(getattr(obj, col)) for col in colnames]
        formatter.rows(row)


class TableFormatter:       # Acts as a design specification
    def headings(self, headers):
        raise NotImplementedError

    def rows(self, row):
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for header in headers:
            print(f'{header:>10}', end='')
        print()

    def rows(self, row):
        for item in row:
            print(f'{item:>10}', end='')
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def rows(self, row):
        print(','.join(row))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for header in headers:
            print(f'<th>{header}</th>', end='')
        print('</tr>')

    def rows(self, row):
        print('<tr>', end='')
        for item in row:
            print(f'<td>{item}</td>', end='')
        print('<tr>')


class Quoted:
    def rows(self, row):
        r = [f'"{item}"' for item in row]
        super().rows(r)


class QuotedFormatter(Quoted, TextTableFormatter):
    pass


text_formatter = TextTableFormatter()
csv_formatter = CSVTableFormatter()
print_table(data, ['price', 'shares', 'name'], text_formatter)