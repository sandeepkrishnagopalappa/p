import random
import csv
import time
with open('stocks.csv') as f:
    records = []
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        records.append({header: item for header, item in zip(headers, row)})
while True:
    for item in records:
        f = open('test.log', 'a')
        data = ','.join(list(item.values()))
        f.write(data)
        f.write('\n')
        time.sleep(random.randint(1, 5))
        f.close()
