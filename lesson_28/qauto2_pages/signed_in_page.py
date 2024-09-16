from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28.qauto2_pages.base_page import BasePage
from lesson_28.qauto2_pages.ui_elements import UIElements


class SignedInPage(BasePage):
    def __init__(self, driver):
        super(SignedInPage, self).__init__(driver)
        self.ui = UIElements()

    def verify_page_loaded(self):
        WebDriverWait(self.driver, 5).until(EC.url_contains("/panel/garage"))

    def get_empty_garage_message(self):
        return self.find_element(self.ui.after_register_msg).text

    def verify_empty_garage_message(self, email):
        message = self.get_empty_garage_message()
        assert message == "You don’t have any cars in your garage", "Empty garage message did not match"
        print(f' User {email} is registered!')