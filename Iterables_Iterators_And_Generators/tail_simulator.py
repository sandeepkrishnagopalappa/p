import random
import time
stocks = [
    {"name": "AA", "price": 14.64, "change": -0.12, "high": 15.02, "low": 14.30},
    {"name": "IBM", "price": 109.34, "change": +0.89, "high": 109.48, "low": 108.20},
    {"name": "MSFT", "price": 150.26, "change": +1.2, "high": 150.89, "low": 150.14},
    {"name": "DXC", "price": 13.67, "change": -1.3, "high": 13.76, "low": 13.56},
    {"name": "HP", "price": 16.69, "change": +0.1, "high": 16.96, "low": 16.39},
    {"name": "GOOG", "price": 1115.94, "change": +2.3, "high": 1116.94, "low": 1114.94},
    {"name": "GE", "price": 37.30, "change": -0.02, "high": 38.12, "low": 36.30},
    {"name": "INTC", "price": 21.85, "change": +0.02, "high": 22.85, "low": 20.85},
    {"name": "AIG", "price": 71.50, "change": -0.03, "high": 72.50, "low": 70.50},
    {"name": "CAT", "price": 78.88, "change": +0.36, "high": 79.88, "low": 77.88},
]
while True:
    for item in stocks:
        f = open('/home/sandeep/Desktop/test.log', 'a')
        f.write(f'{item["name"]}, {item["price"]}, {item["change"]}, {item["high"]}, {item["low"]}')
        f.write('\n')
        time.sleep(random.randint(1, 5))
        f.close()