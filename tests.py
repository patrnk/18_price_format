import unittest
from unittest.mock import patch

import format_price


class FormatCorrectPriceTestCase(unittest.TestCase):

    def run_test(self, inputs, expected_outputs):
        for input_index, input_value in enumerate(inputs):
            output = format_price.format_price(input_value)
            self.assertEqual(output, expected_outputs[input_index])
    
    def test_format_price_formats_integers(self):
        inputs = ['5.000000', '3245.000000', '3003245.000000']
        expected_outputs = ['5', '3 245', '3 003 245']
        self.run_test(inputs, expected_outputs)

    def test_format_price_formats_floats(self):
        inputs = ['0.000000', '0.000001', '5.000001', '3245.003000', '3003245.100000']
        expected_outputs = ['0', '5,000001', '3 245,003', '3 003 245,1']
        self.run_test(inputs, expected_outputs)


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

    def run_test(self, inputs, expected_output):
        for input_index, input_value in enumerate(inputs):
            output = format_price.is_correctly_formatted(input_value)
            self.assertEqual(output, expected_output)

    def test_is_correctly_formatted_returns_true(self):
        inputs = ['0.000000', '0.000001', '5.000000', 
                  '3245.001000', '3003245.999999']
        self.run_test(inputs, True)

    def test_is_correctly_formatted_returns_false(self):
        inputs = ['0005.000000', '3245', '-3003245.999999',
                  'Agent 007', 'NaN', '123.456', '123.E4',
                  '.1', '+5.000000', 'infinity','53.', '1e1']
        self.run_test(inputs, False)


if __name__ == '__main__':
    unittest.main()
