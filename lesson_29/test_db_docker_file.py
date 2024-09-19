import allure
import pytest


def test_database_connection(setup_database):
    cursor = setup_database
    assert cursor.connection is not None
    pass


def test_data_insertion(setup_database):
    cursor = setup_database

    cursor.execute("""
        INSERT INTO users (first_name, last_name, status) 
        VALUES 
            ('John', 'Johnson', 'registered'), 
            ('Thomas', 'Thomson', 'active'),
            ('Peter', 'Peterson', 'inactive'),
            ('Harry', 'Harrison', 'active'),
            ('Robin', 'Robinson', 'deleted')
    """)
    cursor.connection.commit()

    cursor.execute("""
        SELECT id, first_name, last_name, status
        FROM users
        WHERE status IN ('deleted', 'active')
    """)

    users = cursor.fetchall()

    expected_data = (id, 'Harry', 'Harrison', 'active')
    assert expected_data in [(id, first_name, last_name, status) for (user_id, first_name, last_name, status) in
                             users]
    pass
