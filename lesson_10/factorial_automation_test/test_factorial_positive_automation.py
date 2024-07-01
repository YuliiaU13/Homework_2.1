import pytest

from lesson_10.Lesson10_functions import factorial


@pytest.mark.positive
@pytest.mark.smoke
def test_factorial():
    assert factorial(3) == 6

