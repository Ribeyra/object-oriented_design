class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
        }
    # BEGIN (write your solution here)

    def __init__(self, **options):
        self.instance_options = self.OPTIONS.copy()
        if options:
            self.instance_options.update(options)

    def validate(self, psswrd):
        res = {}
        if self.instance_options['contain_numbers'] is True:
            for el in psswrd:
                if el.isdigit():
                    break
            else:
                res['contain_numbers'] = 'should contain at least one number'
        if len(psswrd) < self.instance_options['min_len']:
            res['min_len'] = 'too small'
        return res
    # END

    def _has_number(self, password):
        return any(char.isdigit() for char in password)


validator = PasswordValidator(contain_numberz=None)
y = validator.validate('qwertya3sdf')
x = validator.validate('qwerty')
print(x)
