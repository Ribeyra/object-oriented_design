class Obj:
    def __init__(self, data):
        self.data = dict(map(
            lambda x:
            (x[0], self.__class__(x[1]))
            if isinstance(x[1], dict)
            else x,
            data.items()
        ))

    def __getitem__(self, key):
        value = self.data.get(key)
        if isinstance(value, dict):
            return self.__class__(value)
        return value

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getattr__(self, key):
        return self.data.get(key)

    def __setattr__(self, key, value):
        if key != 'data':
            self.__setitem__(key, value)
        else:
            super().__setattr__(key, value)

    def __repr__(self):
        return str(self.data)


items = {
    'key': 'value',
    'key2': {
        'key3': 'value3'
    }
}

obj = Obj(items)
print(obj.key)
obj.key = 'new_value'
print(obj['key'])
