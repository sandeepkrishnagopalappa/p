import csv

class Covid:
    def __init__(self):
        self.records = []

    def add_case(self, country, _date, cases):
        self.records.append({"country": country, "_date": _date, "cases": int(cases)})

    def total_cases(self):
        return sum([record['cases'] for record in self.records])

    def cases_by_country(self):
        from collections import defaultdict
        d = defaultdict(int)
        for record in self.records:
            d[record['country']] += record['cases']
        return d


with open('covid_data.csv', 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)    # Skipping Headers
    c = Covid()
    for row in rows:
        c.add_case(row[2], row[3], row[5])
    print(c.total_cases())
    print(c.cases_by_country())
