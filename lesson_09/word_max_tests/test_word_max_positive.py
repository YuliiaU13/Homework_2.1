import unittest

from lesson_09.homeworks import word_max


class WordMaxPositiveTest(unittest.TestCase):

    def test_word_max_positive(self):

        result = word_max(['lesson', 'less', 'LA'])
        self.assertEqual(result, 'lesson')