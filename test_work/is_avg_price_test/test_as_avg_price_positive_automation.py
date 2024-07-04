import pytest

from test_work.functions import get_avg_price

from test_work.functions import journal_list
from test_work.functions import volume_param

journal_list_all_more10000 = [
    {"name": "National Geographic", "volume": 15000, "price": 7.99},
    {"name": "Time", "volume": 20000, "price": 5.99},
    {"name": "Vogue", "volume": 18000, "price": 6.99}
]

journal_list_all_less10000 = [
    {"name": "National Geographic", "volume": 8000, "price": 7.99},
    {"name": "Time", "volume": 5000, "price": 5.99},
    {"name": "Vogue", "volume": 7000, "price": 6.99}
]


journal_list_all_zero_cost = [
    {"name": "National Geographic", "volume": 11000, "price": 0},
    {"name": "Time", "volume": 12000, "price": 0},
    {"name": "Vogue", "volume": 10500, "price": 0}
]


input_data_3 = (journal_list, journal_list_all_more10000,
              journal_list_all_less10000, journal_list_all_zero_cost)
expected_data_3 = (6.82, 6.99, 0, 0)


@pytest.mark.parametrize('input_data_3, expected_data_3', list(zip(input_data_3, expected_data_3)),
                         ids=('task_data', 'all_more10000', 'all_less10000', 'all_zero_cost'))
def test_get_avg_price_positive(input_data_3, expected_data_3):
    assert get_avg_price(input_data_3, volume_param) == expected_data_3

