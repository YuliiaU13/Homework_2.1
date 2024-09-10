import os
from dotenv import load_dotenv
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()


class NovaPoshtaTracking:
    def __init__(self, driver):
        self.driver = driver
        self.url = os.getenv("NEW_POST")

    def open_tracking_page(self):
        self.driver.get(self.url)

    def enter_tracking_number(self, tracking_number):
        tracking_input = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Номер посилки"]'))
        )
        tracking_input.clear()
        tracking_input.send_keys(tracking_number)
        tracking_input.send_keys(Keys.RETURN)

        # alternate way is to use button "Пошук" instead to Enter:
        # search_button = WebDriverWait(self.driver, 5).until(
        #     EC.element_to_be_clickable((By.ID, "np-number-input-desktop-btn-search-en"))
        # )
        # search_button.click()

    def get_status(self):
        try:
            status_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header__status-text"))
            )
            return status_element.text
        except TimeoutException:
            error_element = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='tracking__error-text']"))
            )
            return error_element.text

    def close(self):
        self.driver.quit()
