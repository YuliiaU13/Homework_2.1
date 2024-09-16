import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


class BasePage:
    def __init__(self, driver):
        self.url = os.getenv("QAUTO2")
        self.driver = driver

    def find_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
