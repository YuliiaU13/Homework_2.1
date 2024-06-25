import unittest

from lesson_09.homeworks import cost_item


class CostItemPositiveTest(unittest.TestCase):

    def test_cost_item_positive(self):

        result = cost_item(1179, 18)
        self.assertEqual(result, 21222)