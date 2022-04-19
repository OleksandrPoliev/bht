from django.core.exceptions import ValidationError


def ISBN_validator(value):
    if len(str(value))!=13:
        raise ValidationError(f'{value} min len is 13!')
