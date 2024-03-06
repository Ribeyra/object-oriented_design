""" class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other):
        return self.id == other.id


# Создаем двух пользователей с одинаковым именем и идентификатором.
user1 = User(1, 'John')
user2 = User(1, 'Nohn')

user3 = User(3, 'John')

print(user1 == user2)  # Вывод: True
print(user1 == user3)  # Вывод: False """


""" class Money:
    default_currency = 'USD'
    exchange_rates = {'USD': 1}

    def __init__(self, quantity, currency='USD', exchange_rates=False):
        self.currency = currency
        self.quantity = quantity
        if currency not in self.exchange_rates:
            self.exchange_rates[currency] = (
                exchange_rates if exchange_rates else 1
            )

    def set_exchange(self, value):
        self.exchange_rates[self.currency] = value

    set_exchange = property(fset=set_exchange)

    def __repr__(self):
        return f'{self.quantity} {self.currency}'

    def view_exchange(self):
        return self.exchange_rates[self.currency]

    def __eq__(self, other):
        value_1 = self.exchange_rates[self.currency] * self.quantity
        value_2 = self.exchange_rates[other.currency] * other.quantity
        return value_1 == value_2


wallet_1 = Money(130)
wallet_2 = Money(100, 'EUR')
wallet_2.set_exchange = 1.3
print(wallet_1 == wallet_2) """


from urllib.parse import urlparse, parse_qs     # noqa e402


class Url:
    def __init__(self, adress):
        values = urlparse(adress)
        self.scheme = values[0]

        hostname = values[1]
        if hostname[-1].isdigit():
            hostname = hostname.split(':')[0]
        self.hostname = hostname
        self.query_params = parse_qs(values[4])

    def get_scheme(self):
        return self.scheme

    def get_hostname(self):
        return self.hostname

    def get_query_params(self):
        return self.query_params

    def get_query_param(self, key, default=None):
        if key in self.query_params:
            return self.query_params[key][0]
        return default

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


s = Url('http://hexlet.io:80?key=value&key2=value2')
print(s.get_query_param('key'))
