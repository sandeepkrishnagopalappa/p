import csv
import tracemalloc
import time

_cache = {}


def measure_memory(func, *args):
    tracemalloc.start()
    result = func(*args)
    print('Memory: ', tracemalloc.get_traced_memory())
    tracemalloc.stop()
    return result


def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    stop = time.time()
    print('Time: ', stop - start)
    return result


def make_record(headers, row):
    return {h: r for h, r in zip(headers, row)}


def make_cache(row, index):
    if row[index] in _cache:
        row[index] = _cache[row[index]]
    else:
        _cache[row[index]] = row[index]


def record(filename):
    data = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip Headers
        for row in rows:
            make_cache(row, 1)
            make_cache(row, 2)
            data.append(make_record(headers, row))
    return data


mem_result = measure_memory(record, 'chicago.csv')
t_result = measure_time(record, 'chicago.csv')