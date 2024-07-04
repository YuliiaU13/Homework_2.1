import pytest

from test_work.functions import get_avg_price
from test_work.functions import volume_param

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

input_data_2 = (journal_list_volume_string,
                'journal_list_volume_string',
                journal_list_volume_no_price)
expected_data_2 = (TypeError, TypeError, TypeError)


@pytest.mark.parametrize('input_data_2, expected_data_2',
                         list(zip(input_data_2, expected_data_2)),
                         ids=('volume_is_string', 'data_is_string', 'volume_no_price'))
def test_get_avg_price_negative_type_err(input_data_2, expected_data_2):
    with pytest.raises(expected_data_2):
        assert get_avg_price(input_data_2)
