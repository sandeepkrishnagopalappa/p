import random
import time
with open('stocks.csv') as f:
    for line in f:
        ff = open("airline_live.log", 'a')
        ff.write(line)
        time.sleep(random.randint(1, 5))
        ff.close()