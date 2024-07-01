import pytest

from lesson_10.Lesson10_functions import find_primes


@pytest.mark.positive
def test_find_primes():
    assert find_primes(10) == [2, 3, 5, 7]
