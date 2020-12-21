import csv
from collections import Counter

filename = 'covid_data.csv'


# Making a Class Defnition
class Covid:
    def __init__(self, row):
        self.country = row[2]
        self.date_ = row[3]
        self.cases = int(row[5])


class Data:
    def __init__(self):
        self._records = []

    def __len__(self):
        return len(self._records)

    def __iter__(self):
        return iter(self._records)

    def __getitem__(self, index):
        return self._records[index]

    @classmethod
    def from_csv(cls, filename):
        self = cls()
        with open(filename, 'r') as f:
            rows = csv.reader(f)
            next(rows)  # Skipping Headers
            for row in rows:
                self._records.append((Covid(row)))
        return self

    @property
    def countries_affected(self):
        return {item.country for item in self._records}

    @property
    def total_cases_per_country(self):
        c = Counter()
        for item in self._records:
            c[item.country] += item.cases
        return c


d = Data.from_csv(filename)