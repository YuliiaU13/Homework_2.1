import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
from lesson_28.qauto2_pages.registration_page import RegistrationPage
from lesson_28.qauto2_pages.signed_in_page import SignedInPage

load_dotenv()


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.get(os.getenv("QAUTO2"))
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def registration_page(driver):
    return RegistrationPage(driver)


@pytest.fixture
def signed_in_page(driver):
    return SignedInPage(driver)


@pytest.fixture(scope='session')
def name():
    return "John"


@pytest.fixture(scope='session')
def last_name():
    return "Johnson"


@pytest.fixture(scope='session')
def email():
    return "john.john@johnny.com"


@pytest.fixture(scope='session')
def password():
    return "Password7"

