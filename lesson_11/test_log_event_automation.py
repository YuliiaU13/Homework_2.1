
from lesson_11.homework_10 import log_event

def test_success():
    log_event('Alex', 'success')
    assert True


def test_expired():
    log_event('Ann Kathrine', 'expired')
    assert True


def test_error():
    log_event('Mike', '')
    assert True


def test_no_name():
    log_event('', 'expired')
    assert True


def test_no_status():
    log_event('', '')
    assert True


# input_ = (('Alex', 'success'), ('Ann Kathrine', 'expired'),
#           ('Mike', ''), ('', 'expired'), ('', ''))
# expected = ('True', 'True', 'True', 'True', 'True')
#
#
# @pytest.mark.parametrize('input_, expected', list(zip(input_, expected)))
# def test_log_event(input_, expected):
#     assert True
