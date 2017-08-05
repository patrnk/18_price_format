import unittest
from unittest.mock import patch

import format_price


class FormatCorrectPriceTestCase(unittest.TestCase):

    @patch.object(format_price, 'insert_space_every_three_digits', return_value='3 245')
    @patch.object(format_price, 'is_correctly_formatted', return_value=True)
    def test_format_price_returns_integer_without_fraction(self, patched_checked, patched_formatter):
        test_input = '3245.000000'
        expected_output = '3 245'
        output = format_price.format_price(test_input)
        self.assertEqual(output, expected_output)

    @patch.object(format_price, 'insert_space_every_three_digits', return_value='3 245')
    @patch.object(format_price, 'is_correctly_formatted', return_value=True)
    def test_format_price_returns_float_without_trailing_zeroes(self, patched_checker, patched_formatter):
        test_input = '3245.003400'
        expected_output = '3 245,0034'
        output = format_price.format_price(test_input)
        self.assertEqual(output, expected_output)


class FormatIncorrectPriceTestCase(unittest.TestCase):

    def run_test(self, inputs, expected_error):
        for test_input in inputs:
            with self.assertRaises(expected_error):
                format_price.format_price(test_input)
        
    def test_format_price_raises_type_error(self):
        inputs = [42, True, [], {}]
        self.run_test(inputs, TypeError)

    @patch.object(format_price, 'is_correctly_formatted', return_value=False)
    def test_format_price_raises_value_error(self, patched_is_correctly_formatted):
        inputs = ['Incorrect price']
        self.run_test(inputs, ValueError)


class IsCorrectlyFormattedTestCase(unittest.TestCase):

    def test_is_correctly_formatted_returns_true_for_zero(self):
        test_input = '0.000000'
        output = format_price.is_correctly_formatted(test_input)
        self.assertTrue(output)

    def test_is_correctly_formatted_returns_true_for_typical_float(self):
        test_input = '3245.001200'
        output = format_price.is_correctly_formatted(test_input)
        self.assertTrue(output)

    def test_is_correctly_formatted_returns_true_for_integer(self):
        test_input = '123.000000'
        output = format_price.is_correctly_formatted(test_input)
        self.assertTrue(output)

    def test_is_correctly_formatted_returns_false_for_leading_zeros(self):
        test_input = '0005.000000'
        output = format_price.is_correctly_formatted(test_input)
        self.assertFalse(output)

    def test_is_correctly_formatted_returns_false_for_integer_without_decimal_point(self):
        test_input = '3245'
        output = format_price.is_correctly_formatted(test_input)
        self.assertFalse(output)

    def test_is_correctly_formatted_returns_false_for_negative_float(self):
        test_input = '-123.100000'
        output = format_price.is_correctly_formatted(test_input)
        self.assertFalse(output)

    def test_is_correctly_formatted_returns_false_for_arbitrary_string(self):
        test_input = 'Agent 007'
        output = format_price.is_correctly_formatted(test_input)
        self.assertFalse(output)

    def test_is_correctly_formatted_returns_false_for_nan(self):
        test_input = 'NaN'
        output = format_price.is_correctly_formatted(test_input)
        self.assertFalse(output)

    def test_is_correctly_formatted_returns_false_for_fraction_in_scientific_notation(self):
        test_input = '123.E4'
        output = format_price.is_correctly_formatted(test_input)
        self.assertFalse(output)

    def test_is_correctly_formatted_returns_false_for_fraction_without_integer_part(self):
        test_input = '.1'
        output = format_price.is_correctly_formatted(test_input)
        self.assertFalse(output)

    def test_is_correctly_formatted_returns_false_for_plus_sign(self):
        test_input = '+5.000000'
        output = format_price.is_correctly_formatted(test_input)
        self.assertFalse(output)

    def test_is_correctly_formatted_returns_false_for_integer_without_fraction_part(self):
        test_input = '53.'
        output = format_price.is_correctly_formatted(test_input)
        self.assertFalse(output)

    def test_is_correctly_formatted_returns_false_for_integer_in_scientific_notation(self):
        test_input = '1e1'
        output = format_price.is_correctly_formatted(test_input)
        self.assertFalse(output)

    def test_is_correctly_formatted_returns_false_for_double_decimal_dot(self):
        test_input = '0..0'
        output = format_price.is_correctly_formatted(test_input)
        self.assertFalse(output)


class InsertSpaceEveryThreeDigitsTestCase(unittest.TestCase):

    def test_insert_space_every_three_digits_correct_for_nine_digits(self):
        test_input = '123456789'
        expected_output = '123 456 789'
        output = format_price.insert_space_every_three_digits(test_input)
        self.assertEqual(output, expected_output)

    def test_insert_space_every_three_digits_correct_for_eight_digits(self):
        test_input = '12345678'
        expected_output = '12 345 678'
        output = format_price.insert_space_every_three_digits(test_input)
        self.assertEqual(output, expected_output)

    def test_insert_space_every_three_digits_correct_for_seven_digits(self):
        test_input = '1234567'
        expected_output = '1 234 567'
        output = format_price.insert_space_every_three_digits(test_input)
        self.assertEqual(output, expected_output)

    def test_insert_space_every_three_digits_correct_for_one_digit(self):
        test_input = '1'
        expected_output = '1'
        output = format_price.insert_space_every_three_digits(test_input)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
