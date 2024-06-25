import unittest

from lesson_09.homeworks import word_max


class WordMaxNegativeTest(unittest.TestCase):

    def test_word_max_negative(self):
        expected_message = "word_max_tests() takes 1 positional argument but 3 were given"
        with self.assertRaises(TypeError) as type_error:
            result = word_max('lesson', 'less', 'LA')

        error = type_error.exception
        error_message = error.args[0]
        self.assertEqual(error_message, expected_message)
        pass
