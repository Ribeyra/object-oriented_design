"""
# Класс при создании экземпляра получает дату и функции-предикаты. Предикаты
# доступны всем экземплярам класса. Метод is_valid, является предикатом.
# Проверка проводится по всем предикатам, названия которых перечисленны в
# качестве аргумента, либо по всем предикатам, доступным классу, если метод
# вызван без аргумента
class DataValidator:
    validators = {}

    def __init__(self, data, *validators):
        if validators:
            for valid_foo in validators:
                value = {valid_foo.__name__: valid_foo}
                self.validators.update(value)
        self.data = data

    def is_valid(self, *funcs):
        if not funcs:
            funcs = self.validators.keys()

        for valid_foo in funcs:
            if not self.validators[valid_foo](self.data):
                return False
        else:
            return True


def len_8(value):
    if len(value) < 8:
        return False
    return True


def has_num(value):
    for el in value:
        if el.isdigit():
            return True
    else:
        return False


pass_1 = DataValidator('asdfrtegety', len_8, has_num)
print(pass_1.is_valid('has_num'))       # False
pass_2 = DataValidator('123141asdawd')
print(pass_2.is_valid())                # True
 """


""" class DataValidator:
    def __init__(self, data):
        self.data = data
        self.errors = []

    def validate_email(self):
        if '@' not in self.data.get('email', ''):
            self.errors.append('email error')
        return self

    def validate_pass(self):
        if len(self.data.get('pass', '')) < 8:
            self.errors.append('Pass too short')
        return self

    def get_errors(self):
        return self.errors


data = {'email': 'test@test.ru', 'pass': '123'}
asas = DataValidator(data)
asas.validate_email()
print(asas.get_errors())
asas.validate_pass()
print(asas.get_errors())
data2 = {'email': 'john_cena', 'pass': '123'}
john = DataValidator(data2)
print(john.validate_email().validate_pass().get_errors()) """

from datetime import date   # noqa e402


class Booking:
    def __init__(self):
        self.booked_days = set()    # забронированные дни хранятся в множестве

    def book(self, begin, end):
        """
        toordinal() возвращает номер дня от начала календаря.
        Пр. 2008-11-14 -> 733360
        """
        begin = date.fromisoformat(begin).toordinal()
        end = date.fromisoformat(end).toordinal()
        """
        получаем множество дней из диапазона нового бронирования
        """
        new_booking = set(range(begin, end))
        """
        если множество пустое, значит конец периода раньше или равен началу,
        бронирование невозможно
        """
        if not new_booking:
            return False
        """
        если в результате пересечания получилось не пустое множество, значит
        бронирование невозможно
        """
        if self.booked_days & new_booking:
            return False
        self.booked_days.update(new_booking)
        return True


x = date.fromisoformat('2008-11-14').toordinal()
s = date.fromisoformat('2008-11-15').toordinal()
set1 = set(range(x, s))
# y = date.fromisoformat('2008-11-15').toordinal()
# z = date.fromisoformat('2008-11-20').toordinal()
# set2 = set(range(y, z))
print(set1)
# booking = Booking()
# print(booking.book('2008-11-11', '2008-11-13'))  # True
# print(booking.book('2008-11-12', '2008-11-12') ) # False
# print(booking.book('2008-11-10', '2008-11-12') ) # False
# print(booking.book('2008-11-12', '2008-11-14') ) # False
# print(booking.book('2008-11-10', '2008-11-11') ) # True
# print(booking.book('2008-11-13', '2008-11-14'))  # True
