import pytest
import logging

logging.basicConfig(level=logging.INFO, filename='test_search.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TestCarAPI:
    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 7),
        (None, 10),
        ("brand", None),
        ("price", None),
        (None, None)
    ])
    def test_get_cars(self, session_with_auth, sort_by, limit):
        base_url = "http://127.0.0.1:8080"
        params = {}
        if sort_by:
            params['sort_by'] = sort_by
        if limit:
            params['limit'] = limit

        response = session_with_auth.get(f"{base_url}/cars", params=params)
        assert response.status_code == 200, f"Request failed with status {response.status_code}"

        cars = response.json()
        logging.info(f"{len(cars)} cars are gotten, sorting parameters: sort_by={sort_by}, limit={limit}")
        logging.info(f"The first car: {cars[0] if cars else 'There are no cars'}")

        assert isinstance(cars, list), "Response is not a list"
        if limit:
            assert len(cars) <= limit, f"Returned more cars than limit {limit}"