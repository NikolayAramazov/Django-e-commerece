from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PhoneNumberValidator:

    def __init__(self, exact_length):
        self.exact_length = exact_length

    def __call__(self, value):
        if not value.isdigit():
            raise ValidationError('Phone number must contain only digits')

        if self.exact_length != len(value):
            raise ValidationError(f'Phone number must contain exactly {self.exact_length} digits')

@deconstructible
class ZipCodeValidator:

    def __init__(self, exact_length):
        self.exact_length = exact_length

    def __call__(self, value):
        if not value.isdigit():
            raise ValidationError('Zip code must contain only digits')

        if self.exact_length != len(value):
            raise ValidationError(f'Zip code must contain exactly {self.exact_length} digits')