class Pirozhok:
    pass


def to_Klass(data):
    object_ = Pirozhok()
    object_.__dict__.update(data)
    return object_


data = {
    'key': 'value',
    'key2': 'value2',
}
config = to_Klass(data)

print(type(config))
print(config.key)   # value
print(config.key2)  # value2
