import unittest

from lesson_09.homeworks import vice_versa


class ViceVersaNegativeTest(unittest.TestCase):

    def test_vice_versa_negative(self):
        expected_message = "'int' object is not subscriptable"
        with self.assertRaises(TypeError) as type_error:
            result = vice_versa(123456)

        error = type_error.exception
        error_message = error.args[0]
        self.assertEqual(error_message, expected_message)
        pass
