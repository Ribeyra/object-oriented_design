class Pirozhok:
    pass


def to_Klass(data) -> Pirozhok:
    object_ = Pirozhok()
    object_.__dict__ = data
    return object_


data = {
    'key': 'value',
    'key2': 'value2',
}
config = to_Klass(data)

print(type(config))   # value
print(config.key2)  # value2
