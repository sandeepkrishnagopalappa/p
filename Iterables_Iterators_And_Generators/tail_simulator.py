import random
import csv
import time
with open('stocks.csv') as f:
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        ff = open("test.log", 'a')
        ff.write(",".join(row))
        ff.write("\n")
        time.sleep(random.randint(1, 5))
        ff.close()