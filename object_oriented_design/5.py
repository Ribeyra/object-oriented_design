""" class Collection:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return str(self.lst)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.values):
            result = self.values[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def map(self, foo):
        for i in range(len(self.lst)):
            self.lst[i] = foo(self.lst[i])
        return Collection(self.lst)

    def reject(self, foo):
        res = []
        for el in self.lst:
            if not foo(el):
                res.append(el)
        self.lst = res
        return Collection(self.lst)

    def all(self):
        return self.__str__()


names = Collection(['taylor', 'abigail', None])

result = names\
    .map(lambda name: str(name).upper() if name else '')\
    .reject(lambda name: name == '')

# Выводим коллекцию на экран
print(result.all())  # => ['TAYLOR', 'ABIGAIL'] """


class Collection:
    def __init__(self, coll):
        self.coll = coll

    def map(self, foo):
        self.coll = list(map(foo, self.coll))
        return self

    def reject(self, foo):
        self.coll = list(filter(foo, self.coll))
        return self

    def all(self):
        return self.coll


names = Collection(['taylor', 'abigail', None])

result = names\
    .map(lambda name: str(name).upper() if name else '')\
    .reject(lambda name: name == '')

# Выводим коллекцию на экран
print(result.all())  # => ['TAYLOR', 'ABIGAIL']
