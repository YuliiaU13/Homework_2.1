import logging

import pytest
from lesson_11.homework_10 import log_event


# @pytest.mark.parametrize('status', ['success', 'expired', '', None, 123])
# def test_log_event_status(status):
#     log_event('user_name', status)
#
#
# @pytest.mark.parametrize('username', ['Alex', 'John Mitch', '', None, 123])
# def test_log_event_username(username):
#     log_event(username, 'success')


usernames = ['Alex', 'John Mitch', '', None, 123]
statuses = ['success', 'expired', '', None, 123]


@pytest.mark.parametrize('username, status', list(zip(usernames, statuses)))
def test_log_event(username, status):
    log_event(username, status)

    with open('login_system.log', 'r') as f:
        logs = f.readlines()
    assert f"Login event - Username: {username}, Status: {status}" in logs[-1]
