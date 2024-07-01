import pytest

from lesson_10.Lesson10_functions import convert_to_24_hour

input_convert = ('11:59 AM', '00:00 AM', '00:01 AM', '06:30 AM',
                 '00:00 PM', '00:01 PM', '06:35 PM', '11:59 PM')
expected = ('11:59', '00:00', '00:01', '06:30',
            '12:00', '12:01', '18:35', '23:59')

io_params = list(zip(input_convert, expected))


@pytest.mark.convert_time
@pytest.mark.parametrize('input_convert, expected', io_params, ids=input_convert)
def test_convert_to_24_hour1(input_convert, expected):
    assert expected == convert_to_24_hour(input_convert)
