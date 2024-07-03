import pytest

from test_work.functions import is_palindrome


@pytest.mark.negative
def test_is_palindrome_int():
    with pytest.raises(AttributeError):
        assert is_palindrome(1221)


def test_is_palindrome_list():
    with pytest.raises(AttributeError):
        assert is_palindrome([])


def test_is_palindrome_tuple():
    with pytest.raises(TypeError):
        assert is_palindrome('f', 2)


def test_is_palindrome_bool():
    with pytest.raises(AttributeError):
        assert is_palindrome(True)
