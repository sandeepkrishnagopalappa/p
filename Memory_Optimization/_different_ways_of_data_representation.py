import csv
from collections import namedtuple
from dataclasses import dataclass
from collections import Counter
import tracemalloc


def memory(func):
    def wrapper(*args):
        tracemalloc.start()
        result = func(*args)
        print('Memory: ', tracemalloc.get_traced_memory())
        tracemalloc.stop()
        return result
    return wrapper


# Makes List of tuples
def make_tuple(row):
    return tuple((row[1], row[2], int(row[4]), row[7]))


# Make Dictionary
def make_dict(row):
    return {
        'country': row[1],
        '_date': row[2],
        'cases': int(row[4]),
        'per_mil': row[7]
    }


# Make Class Instance
class Covid:
    def __init__(self, country, _date, cases, per_mil):
        self.country = country
        self._date = _date
        self.cases = int(cases)
        self.per_mil = float(per_mil)


# Namedtuple
Covid = namedtuple("Covid", ['country', 'date', 'cases', 'per_mil'])


# Data Classes
@dataclass
class Covid:
    country: str
    cases: str
    _date: str
    per_mil: str


def make_instance(row):
    return Covid(row[1], row[2], int(row[4]), row[7])


@memory
def read_csv(filename, record_type):
    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)    # Skipping Headers
        for row in rows:
            records.append(record_type(row))
    return records


fname = '/Users/sandeep/Documents/python_tutorials/Memory_Optimization/covid-data.csv'

data = read_csv(fname, make_dict)

# Names of countries affected by COVID-19
countries = {item['country'] for item in data}

# Total Number of cases in each country
total_cases = Counter()
for item in data:
    total_cases[item['country']] += int(item['cases'])

# Top 10 countries with maximum number of cases
max_10 = sorted(total_cases.items(), key=lambda item: int(item[-1]))[-10:]

# Country with highest Number of cases
mx = max(total_cases.items(), key=lambda item: int(item[-1]))
mi = min(total_cases.items(), key=lambda item: int(item[-1]))
