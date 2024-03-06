""" class Request:
    def __init__(self, timeout=3):
        self.timeout = timeout

    def get(self, server_name):
        print(f'Ожидаю ответ с {server_name} не дольше {self.timeout}')


request = Request(timeout=10)
response = request.get("<http://example.com>") """


""" class Request:
    timer = 3

    def __init__(self, timeout=3):
        self.timer = timeout

    @property
    def timeout(self):
        return self.timer

    @timeout.setter
    def set_timeout(self, value):
        self.timer = value

    def get(self, server_name):
        print(f'Ожидаю ответ с {server_name} не дольше {self.timer}')


request = Request(timeout=10)
request.set_timeout = 5
response = request.get("<http://example.com>") """


""" class Request:
    def __init__(self, timeout=3):
        self.timeout = timeout

    def get(self, server_name, timeout=None):
        if timeout is None:
            timeout = self.timeout

        print(f'Ожидаю ответ с {server_name} не дольше {timeout}')


request = Request(timeout=10)
response = request.get("<http://example.com>", timeout=4)
response = request.get("<http://example.com>") """


class Truncater:
    OPTIONS = {
        'separator': '...',
        'length': 200,
        }

    def __init__(self, length=None, separator=None):
        self.length = length or self.OPTIONS['length']
        self.separator = separator or self.OPTIONS['separator']

    def truncate(self, text, length=None, separator=None):
        length_ = self.length if length is None else length
        separator_ = self.separator if separator is None else separator
        if len(text) > length_:
            return text[:length_] + separator_
        return text


truncater = Truncater()

s = truncater.truncate('one two')  # one two
print(s)
s = truncater.truncate('one two', length=6)  # one tw...
print(s)
truncater2 = Truncater(length=6, separator='*')
s = truncater2.truncate('one two')  # one tw*
print(s)
