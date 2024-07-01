import pytest

from lesson_10.Lesson10_functions import triangle_area


@pytest.mark.negative
def test_triangle_area_less_parameters():
    with pytest.raises(TypeError):
        assert triangle_area(6, 6)


@pytest.mark.negative
def test_triangle_area_not_numbers():
    with pytest.raises(TypeError):
        assert triangle_area('6', '6', '8')
