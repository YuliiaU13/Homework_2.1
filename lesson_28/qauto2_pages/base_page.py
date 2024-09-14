import os
from dotenv import load_dotenv

load_dotenv()


class BasePage:
    def __init__(self, driver):
        self.url = os.getenv("QAUTO2")
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)
