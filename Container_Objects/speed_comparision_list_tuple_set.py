import time


def _time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('Execution Time ',func.__name__, end_time-start_time)
    return wrapper


@_time
def test_list():
    l = []
    for i in range(50000):
        l.append(i)


@_time
def test_tuple():
    t = tuple()
    for i in range(50000):
        t += (i,)


@_time
def test_set():
    s = set()
    for i in range(50000):
        s.add(i)


# Speed Test - Membership
@_time
def test_membership_list(item, _list):
    print(item in _list)


@_time
def test_membership_tuple(item, _tuple):
    print(item in _tuple)


@_time
def test_membership_set(item, _set):
    print(item in _set)
