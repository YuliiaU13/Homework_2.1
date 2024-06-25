import unittest

from lesson_09.homeworks import vice_versa


class ViceVersaPositiveTest(unittest.TestCase):

    def test_vice_versa_positive(self):

        result = vice_versa('мало сала')
        self.assertEqual(result, 'алас олам')