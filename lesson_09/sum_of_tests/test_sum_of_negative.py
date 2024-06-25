import unittest

from lesson_09.homeworks import sum_of


class SumOfNegativeTest(unittest.TestCase):

    def test_sum_of_negative_none(self):
        expected_message = "unsupported operand type(s) for +: 'NoneType' and 'int'"
        with self.assertRaises(TypeError) as type_error:
            result = sum_of(None, 10)

        error = type_error.exception
        error_message = error.args[0]
        self.assertEqual(error_message, expected_message)

    def test_sum_of_negative_str(self):
        expected_message_2 = 'can only concatenate str (not "int") to str'
        with self.assertRaises(TypeError) as type_error_2:
            result = sum_of('5', 10)

        error = type_error_2.exception
        error_message = error.args[0]
        self.assertEqual(error_message, expected_message_2)