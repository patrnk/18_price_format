import unittest

import format_price


class FormatCorrectPriceTestCase(unittest.TestCase):

    def test_format_price_returns_integer_without_fraction(self):
        test_input = '3245.000000'
        expected_output = '3 245'
        output = format_price.format_price(test_input)
        self.assertEqual(output, expected_output)

    def test_format_price_returns_float_without_trailing_zeroes(self):
        test_input = '3245.003400'
        expected_output = '3 245,0034'
        output = format_price.format_price(test_input)
        self.assertEqual(output, expected_output)

    def test_format_price_returns_zero(self):
        test_input = '0.000000'
        expected_output = '0'
        output = format_price.format_price(test_input)
        self.assertEqual(output, expected_output)


class FormatIncorrectPriceTestCase(unittest.TestCase):

    def test_format_price_raises_type_error(self):
        inputs = [42, True, [], {}]
        for test_input in inputs:
            with self.assertRaises(TypeError):
                format_price.format_price(test_input)
        
    def test_format_price_raises_value_error_for_leading_zeros(self):
        test_input = '0005.000000'
        with self.assertRaises(ValueError):
            output = format_price.format_price(test_input)

    def test_format_price_raises_value_error_for_integer_without_decimal_point(self):
        test_input = '3245'
        with self.assertRaises(ValueError):
            format_price.format_price(test_input)

    def test_format_price_raises_value_error_for_negative_float(self):
        test_input = '-123.100000'
        with self.assertRaises(ValueError):
            format_price.format_price(test_input)

    def test_format_price_raises_value_error_for_arbitrary_string(self):
        test_input = 'Agent 007'
        with self.assertRaises(ValueError):
            format_price.format_price(test_input)

    def test_format_price_raises_value_error_for_nan(self):
        test_input = 'NaN'
        with self.assertRaises(ValueError):
            format_price.format_price(test_input)

    def test_format_price_raises_value_error_for_fraction_in_scientific_notation(self):
        test_input = '123.E4'
        with self.assertRaises(ValueError):
            format_price.format_price(test_input)

    def test_format_price_raises_value_error_for_fraction_without_integer_part(self):
        test_input = '.1'
        with self.assertRaises(ValueError):
            format_price.format_price(test_input)

    def test_format_price_raises_value_error_for_plus_sign(self):
        test_input = '+5.000000'
        with self.assertRaises(ValueError):
            format_price.format_price(test_input)

    def test_format_price_raises_value_error_for_integer_without_fraction_part(self):
        test_input = '53.'
        with self.assertRaises(ValueError):
            format_price.format_price(test_input)

    def test_format_price_raises_value_error_for_integer_in_scientific_notation(self):
        test_input = '1e1'
        with self.assertRaises(ValueError):
            format_price.format_price(test_input)

    def test_format_price_raises_value_error_for_double_decimal_dot(self):
        test_input = '0..0'
        with self.assertRaises(ValueError):
            format_price.format_price(test_input)


if __name__ == '__main__':
    unittest.main()
