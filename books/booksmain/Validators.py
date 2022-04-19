from django.core.exceptions import ValidationError


def ISBN_validator(value):
    if len(str(value))!=13:
        raise ValidationError(f'{value} required len is 13!')
