import csv


class Covid:
    def __init__(self, country, cases, per_million):
        self.country = country
        self.cases = cases
        self.per_million = per_million


filename = '_covid_data.csv'
types = [str, str, int, float]
records = []


def read_csv(filename, types):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)    # Skipping headers
        for row in rows:
            converted = [func(val) for func, val in zip(types, row)]
            country, _date, cases, per_million = converted
            records.append(Covid(country, cases, per_million))
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


print_table(data, ['Country', 'Cases', 'Per_Million'])