import pytest

from test_work.functions import get_avg_price


journal_list_volume_string = [
    {"name": "National Geographic", "volume": '15000', "price": 7.99},
    {"name": "Time", "volume": 20000, "price": 5.99},
    {"name": "Vogue", "volume": 18000, "price": 6.99}
]


journal_list_volume_no_price = [
    {"name": "National Geographic", "volume": '15000'},
    {"name": "Time", "volume": 20000, "price": 5.99},
    {"name": "Vogue", "volume": 18000, "price": 6.99}
]


@pytest.mark.negative
def test_get_avg_price_empty_list():
    with pytest.raises(ZeroDivisionError):
        assert get_avg_price([])


def test_get_avg_price_volume_string():
    with pytest.raises(TypeError):
        assert get_avg_price(journal_list_volume_string)


def test_get_avg_price_data_string():
    with pytest.raises(TypeError):
        assert get_avg_price('journal_list_volume_string')


def test_get_avg_price_no_price():
    with pytest.raises(TypeError):
        assert get_avg_price(journal_list_volume_no_price)