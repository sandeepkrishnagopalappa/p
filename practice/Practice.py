class MyItr:
    def __init__(self, iterable):
        self.start = 0
        self.end = len(iterable)-1
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            item = self.iterable[self.start]
            self.start += 1
            return item


m = MyItr([1, 2, 3, 4, 5])


print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
# print(next(m))

