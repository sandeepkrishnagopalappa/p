import random
import csv
import time
with open('/home/sandeep/Desktop/stocks.csv') as f:
    records = []
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        records.append({header: item for header, item in zip(headers, row)})
while True:
    for item in records:
        f = open('/home/sandeep/Desktop/test.log', 'a')
        data = ','.join(list(item.values()))
        f.write(data)
        f.write('\n')
        time.sleep(random.randint(1, 5))
        f.close()

# Simulating Unix tail and grep commands
def _tail():
    with open('/home/sandeep/Desktop/test.log', 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line


print(f'{"name":>8} {"change":>8}')
for line in _tail():
   record = line.split(',')
   if float(record[4]) < 0:
       print(f'{record[0]: >8} {float(record[4]): >8.2f}')


def _grep(names, line):
    row = line.strip().split(',')
    if row[0] in names:
        yield row


for line in _tail():
    for match in _grep({'IBM', 'AA', 'CAT', 'MSFT'}, line):
        print(line)
