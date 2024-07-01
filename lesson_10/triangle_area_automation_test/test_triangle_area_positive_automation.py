import pytest

from lesson_10.Lesson10_functions import triangle_area


@pytest.mark.positive
def test_triangle_area():
    assert round(triangle_area(6, 6, 6), 3) == 15.588

