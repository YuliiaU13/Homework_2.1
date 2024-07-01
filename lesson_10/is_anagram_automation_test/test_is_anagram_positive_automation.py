import pytest

from lesson_10.Lesson10_functions import is_anagram


@pytest.mark.positive
def test_is_anagram():
    assert is_anagram("age", "eag")

