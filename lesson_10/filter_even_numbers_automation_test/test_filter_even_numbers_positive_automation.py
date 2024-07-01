import pytest

from lesson_10.Lesson10_functions import filter_even_numbers


@pytest.mark.positive
def test_filter_even_numbers():
    filter_even_numbers([2, 3, 4, 5, 2, 9, 10])