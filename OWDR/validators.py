import re

from django.core.exceptions import ValidationError


class NumberValidator(object):

    def __init__(self, min_digits=0):
        self.min_digits = min_digits

    def validate(self, password, user=None):
        if len(re.findall('\d', password)) < self.min_digits:
            raise ValidationError(f'Hasło musi zawierać minimum {self.min_digits} cyfr', code='too_few_numbers')

    def get_help_text(self):
        return f'Hasło musi zawierać minimum następującą liczbę cyfr: {self.min_digits} '


class CapitalValidator(object):

    def __init__(self, min_capitals=0):
        self.min_capitals = min_capitals

    def validate(self, password, user=None):
        if len(re.findall('[A-Z]', password)) < self.min_capitals:
            raise ValidationError(f'Hasło musi zawierać minimum {self.min_capitals} wielkich liter', code='too_few_capitals')

    def get_help_text(self):
        return f'Hasło musi zawierać minimum następującą liczbę wielkich liter: {self.min_capitals}'


class LoweCaseValidator(object):

    def __init__(self, min_lower_case=0):
        self.min_lower_case = min_lower_case

    def validate(self, password, user=None):
        if len(re.findall('[a-z]', password)) < self.min_lower_case:
            raise ValidationError(f'Hasło musi zawierać minimum następującą liczbę małych liter: {self.min_lower_case}', code='too_few_lower_case')

    def get_help_text(self):
        return f'Hasło musi zawierać minimum {self.min_lower_case} małych liter'


class SpecialsValidator(object):

    def __init__(self, min_specials=0):
        self.min_specials = min_specials

    def validate(self, password, user=None):
        if len(re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password)) < self.min_specials:
            raise ValidationError(f'Hasło musi zawierać minimum następującą liczbę znaków specjalnych: {self.min_specials}\nznaki specjalne: ()[\]{{}}|\\`~!@#$%^&*_\-+=;:\'",<>./?', code='too_few_specials')

    def get_help_text(self):
        return f'Hasło musi zawierać minimum {self.min_specials} znaków specjalnych'
