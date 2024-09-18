import os
import psycopg2
import pytest
import time


def wait_for_db():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(os.getenv("DATABASE_URL"))
            return conn
        except psycopg2.OperationalError:
            print(f"Failed to connect, {retries} retries left...")
            retries -= 1
            time.sleep(3)
    raise Exception("Could not connect to the database")


@pytest.fixture(scope='session')
def setup_database():
    conn = wait_for_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            status VARCHAR(20)
        );
    """)
    conn.commit()

    yield cursor
    cursor.close()
    conn.close()
