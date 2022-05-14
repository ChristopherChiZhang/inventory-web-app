from django.core.exceptions import ValidationError


class Utils:
    @staticmethod
    def non_negative(value):
        if value < 0:
            raise ValidationError('Value cannot be negative.')
