import pytest

from lesson_10.Lesson10_functions import find_primes


@pytest.mark.negative
def test_find_primes():
    with pytest.raises(TypeError):
        find_primes('10')
