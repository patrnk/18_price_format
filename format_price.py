def has_decimal_point(price):
    return '.' in price


def consists_of_digits_with_decimal_point(price):
    integer_part, fraction_part = price.split('.')
    return integer_part.isdigit() and fraction_part.isdigit()


def integer_part_without_leading_zeros(price):
    integer_part = price.split('.')[0]
    return len(integer_part) <= 1 or integer_part[0] != '0'


def is_correctly_formatted(price):
    format_checks = [
        has_decimal_point,
        consists_of_digits_with_decimal_point,
        integer_part_without_leading_zeros
    ]
    return all(format_check(price) for format_check in format_checks)


def format_price(price):
    if not isinstance(price, str):
        raise TypeError('Price must be a string')
    if not is_correctly_formatted(price):
        raise ValueError('The price is incorrectly formatted')


if __name__ == '__main__':
    pass
