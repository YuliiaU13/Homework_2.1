import pytest
from requests import Session

@pytest.fixture(scope='class')
def session_with_auth():
    session = Session()
    base_url = "http://127.0.0.1:8080"

    # Аутентифікація
    auth_response = session.post(
        f"{base_url}/auth",
        auth=('test_user', 'test_pass')
    )
    access_token = auth_response.json().get("access_token")
    session.headers.update({'Authorization': f'Bearer {access_token}'})

    yield session
    session.close()