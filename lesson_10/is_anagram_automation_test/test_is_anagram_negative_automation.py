import pytest

from lesson_10.Lesson10_functions import is_anagram


@pytest.mark.negative
def test_is_anagram():
    with pytest.raises(TypeError):
        assert is_anagram(None, False)
