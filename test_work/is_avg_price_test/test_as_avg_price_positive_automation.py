import pytest

from test_work.functions import get_avg_price

from test_work.functions import journal_list

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


def test_get_avg_price():
    assert get_avg_price(journal_list) == 6.82


def test_get_avg_price_all_more10000():
    assert get_avg_price(journal_list_all_more10000) == 6.99


def test_get_avg_price_all_less10000():
    assert get_avg_price(journal_list_all_less10000) == 0


def test_get_avg_price_all_zero_cost():
    assert get_avg_price(journal_list_all_zero_cost) == 0
