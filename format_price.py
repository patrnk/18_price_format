import re


def has_decimal_point(price):
    return '.' in price


def consists_of_digits_with_decimal_point(price):
    integer_part, fraction_part = price.split('.', 1)
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


def insert_space_every_three_digits(string_number):
    reversed_number = string_number[::-1]
    groups_of_three = re.findall('.{1,3}', reversed_number)
    reversed_formatted_number = ' '.join(groups_of_three)
    return reversed_formatted_number[::-1]


def format_price(price):
    if not isinstance(price, str):
        raise TypeError('Price must be a string')
    if not is_correctly_formatted(price):
        raise ValueError('The price is incorrectly formatted')
    integer_part, fraction_part = price.split('.')
    formatted_integer_part = insert_space_every_three_digits(integer_part)
    formatted_fraction_part = fraction_part.rstrip('0')
    if not formatted_fraction_part:
        return formatted_integer_part
    return ','.join((formatted_integer_part, formatted_fraction_part))


if __name__ == '__main__':
    price = input('Enter the price to process (e.g. "3245.000000"): ')
    try:
        formatted_price = format_price(price)
    except ValueError as error:
        print(error)
    else:
        print(formatted_price)
