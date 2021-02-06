import csv
from collections import defaultdict

with open("covid_data.csv") as f:
    records = []
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        records.append({"country": row[2], "date": row[3], "cases": int(row[5])})

# Names of all Countries affected by COVID
list_countries = {record['country'] for record in records}

for country in list_countries:
    print(country)

# Total Number of Cases in each country
d = defaultdict(int)

for record in records:
    d[record['country']] += record['cases']

# Want to Know how many countries have less than 10K cases
countries_less_10K = {country: cases for country, cases in d.items() if cases < 10000}

print(countries_less_10K)
