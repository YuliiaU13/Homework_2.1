import pytest

from lesson_10.Lesson10_functions import filter_even_numbers


@pytest.mark.negative
def test_filter_even_numbers_strings():
    with pytest.raises(TypeError):
        filter_even_numbers(['a', 'b', 'c'])


@pytest.mark.negative
def test_filter_even_numbers():
    with pytest.raises(TypeError):
        filter_even_numbers(['4', '5', 'a'])