import pytest

from test_work.functions import is_palindrome

input_data = ('1221', 'ABBA', 'фііф', ' faar RAAF ', ',,??**!**??,,')
expected_data = (True, True, True, True, True, True)


@pytest.mark.positive
@pytest.mark.parametrize('input_data, expected_data', list(zip(input_data, expected_data)),
                         ids=('int', 'capital', 'cyrillic', 'words_with_space', 'symbols'))
def test_is_palindrome(input_data, expected_data):
    assert expected_data == is_palindrome(input_data)
