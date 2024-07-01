import pytest

from lesson_10.Lesson10_functions import factorial


@pytest.mark.negative
def test_factorial_zero_not_one():
    with pytest.raises(AssertionError):
        assert factorial(0) == 0


@pytest.mark.negative
@pytest.mark.smoke
def test_factorial_string():
    with pytest.raises(TypeError):
        assert factorial('3') == 6


@pytest.mark.negative
def test_factorial_string():
    with pytest.raises(TypeError):
        assert factorial(None) == 9
