import pytest

from lesson_10.Lesson10_functions import convert_to_24_hour


@pytest.mark.negative
def test_convert_to_24_hour_without_minutes():
    with pytest.raises(ValueError):
        assert convert_to_24_hour("05 AM") == '05:00'


@pytest.mark.negative
@pytest.mark.smoke
def test_convert_to_24_hour_without_am_pm():
    with pytest.raises(ValueError):
        assert convert_to_24_hour("13:33") == '13:33'


@pytest.mark.negative
@pytest.mark.xfail(reason='takes another text then "AM", "PM"')
def test_convert_to_24_hour_not_am_pm():
    assert convert_to_24_hour("05:05 evening") == '17:05'


@pytest.mark.negative
@pytest.mark.smoke
@pytest.mark.xfail(reason='takes hours > 12')
def test_convert_to_24_hour_more_12_h():
    assert convert_to_24_hour("15:25 PM") == '15:25'


@pytest.mark.negative
@pytest.mark.xfail(reason='takes minutes > 60')
def test_convert_to_24_hour_more_59_min():
    assert convert_to_24_hour("0:60 PM") == "13:00"
