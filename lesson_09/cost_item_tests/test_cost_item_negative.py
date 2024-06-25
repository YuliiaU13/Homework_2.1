import unittest

from lesson_09.homeworks import cost_item


class CostItemNegativeTest(unittest.TestCase):

    def test_cost_item_negative(self):
        expected_message = "can't multiply sequence by non-int of type 'str'"
        with self.assertRaises(TypeError) as type_error:
            result = cost_item('Two', 'Six')

        error = type_error.exception
        error_message = error.args[0]
        self.assertEqual(error_message, expected_message)
        pass
