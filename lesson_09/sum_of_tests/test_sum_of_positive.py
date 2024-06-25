import unittest

from lesson_09.homeworks import sum_of


class SumOfPositiveTest(unittest.TestCase):

    def test_sum_of_positive_numbers(self):

        result = sum_of(5, 10)
        self.assertEqual(result, 15)

    def test_sum_of_positive_lists(self):

        result = sum_of([5], [10])
        self.assertEqual(result, [5, 10])

    def test_sum_of_positive_strings(self):

        result = sum_of('5', '10')
        self.assertEqual(result, '510')