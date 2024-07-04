import pytest

from test_work.functions import is_palindrome

input_data_1 = (1221, [], True)
expected_data_1 = (AttributeError, AttributeError, AttributeError)


@pytest.mark.negative
@pytest.mark.parametrize('input_data_1, expected_data_1',
                         list(zip(input_data_1, expected_data_1)),
                         ids=('int', 'list', 'bool'))
def test_is_palindrome_negative_ass_err(input_data_1, expected_data_1):
    with pytest.raises(expected_data_1):
        assert is_palindrome(input_data_1)


def test_is_palindrome_negative_tuple():
    with pytest.raises(TypeError):
        assert is_palindrome('f', 2)
