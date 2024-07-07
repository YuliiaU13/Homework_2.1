from lesson_11.homework_10 import log_event
import pytest


@pytest.mark.parametrize('status', ['success', 'expired', '', None, 123])
def test_log_event_status(status):
    log_event('user_name', status)


@pytest.mark.parametrize('username', ['Alex', 'John Mitch', '', None, 123])
def test_log_event_username(username):
    log_event(username, 'success')